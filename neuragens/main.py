from typing import Any
from parse import parse
from neuragens.response import Response

class NeuraGens:
    def __init__(self) -> None:
        self.routes = dict()

    def __call__(self, environ, start_response) -> Any:
        response = Response()
        for path, handler_dict in self.routes.items():
            res = parse(path, environ['PATH_INFO'])
            for request_method, handler in handler_dict.items():
                if environ['REQUEST_METHOD'] == request_method and res:
                    handler(environ, response, **res.named)
                    return response.as_wsgi(start_response)
                
        return response.as_wsgi(start_response)
    
    def route_common(self, path, handler, method_name):
        #{
        #    '/test': {
        #        'GET': handler
        #    }
        #}
        path_name = path or f"/{handler.__name__}"
            
        if path_name not in self.routes:
            self.routes[path_name] = {}

        self.routes[path_name][method_name] = handler
        return handler

    def get(self, path=None):
        def wrapper(handler):
            return self.route_common(path, handler, 'GET')

        return wrapper
    
    def post(self, path=None):
        def wrapper(handler):
            print('OIII')
            return self.route_common(path, handler, 'POST')

        return wrapper
    
    def delete(self, path=None):
        def wrapper(handler):
            return self.route_common(path, handler, 'DELETE')

        return wrapper