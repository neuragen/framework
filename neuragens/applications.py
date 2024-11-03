import types
from typing import Any
from parse import parse
from .requests import Request  # Ajustado para o novo caminho
from .responses import Response  # Ajustado para o novo caminho
import inspect

SUPPORTED_REQ_METHODS = {'GET', 'POST', 'DELETE'}

class NeuraGens:
    def __init__(self, middlewares=[]) -> None:
        self.routes = dict()
        self.middlewares = middlewares
        self.middlewares_for_routes = dict()

    async def __call__(self, scope, receive, send) -> Any:
        assert scope['type'] == 'http'
        response = Response()
        request = Request(scope)  # Usa Request para encapsular 'scope'

        # Executa middlewares globais
        for middleware in self.middlewares:
            if isinstance(middleware, types.FunctionType):
                middleware(request)
            else:
                raise ValueError('You can only pass functions as middlewares!')

        # Procura a rota e executa os middlewares específicos da rota
        for path, handler_dict in self.routes.items():
            res = parse(path, request.path)  # Usa request.path ao invés de scope['path']
            for request_method, handler in handler_dict.items():
                if request.method == request_method and res:  # Usa request.method
                    # Executa middlewares específicos da rota, se existirem
                    route_middlewares = self.middlewares_for_routes.get(path, {}).get(request_method, [])
                    for route_middleware in route_middlewares:
                        if isinstance(route_middleware, types.FunctionType):
                            route_middleware(request)
                        else:
                            raise ValueError('Route middlewares must be functions!')

                    # Chama o handler (sincronamente ou assincronamente)
                    if inspect.iscoroutinefunction(handler):
                        await handler(request, response, **res.named)
                    else:
                        handler(request, response, **res.named)
                    await response.as_asgi(send)
                    return

        # Se nenhuma rota foi encontrada
        await response.as_asgi(send)

    def route_common(self, path, handler, method_name, middlewares):
        path_name = path or f"/{handler.__name__}"

        if path_name not in self.routes:
            self.routes[path_name] = {}

        self.routes[path_name][method_name] = handler

        if path_name not in self.middlewares_for_routes:
            self.middlewares_for_routes[path_name] = {}

        # Armazena middlewares específicos para o método HTTP da rota
        self.middlewares_for_routes[path_name][method_name] = middlewares

        return handler

    def get(self, path=None, middlewares=[]):
        def wrapper(handler):
            return self.route_common(path, handler, 'GET', middlewares)

        return wrapper
    
    def post(self, path=None, middlewares=[]):
        def wrapper(handler):
            return self.route_common(path, handler, 'POST', middlewares)

        return wrapper
    
    def delete(self, path=None, middlewares=[]):
        def wrapper(handler):
            return self.route_common(path, handler, 'DELETE', middlewares)

        return wrapper
    
    def route(self, path=None, middlewares=[]):
        def wrapper(handler):
            if isinstance(handler, type):
                class_members = inspect.getmembers(handler, lambda x: inspect.isfunction(x) and not (
                    x.__name__.startswith("__") and x.__name__.endswith("__")
                ) and x.__name__.upper() in SUPPORTED_REQ_METHODS )
                
                for fn_name, fn_handler in class_members:
                    self.route_common(path or f"/{handler.__name__}", fn_handler, fn_name.upper(),
                                      middlewares)
            else:
                raise ValueError("@route can only be used for classes")
        
        return wrapper
