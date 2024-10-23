from typing import Any

from neuragens.response import Response

class NeuraGens:
    def __init__(self) -> None:
        self.routes = dict()

    def __call__(self, environ, start_response) -> Any:
        response = Response()
        for path, handler_dict in self.routes.items():
            #print(handler_dict)
            for request_method, handler in handler_dict.items():
                if environ['REQUEST_METHOD'] == request_method and path == environ['PATH_INFO']:
                    handler(environ, response)
                    response.as_wsgi(start_response)
                    return [response.text.encode()]
    
    def get(self, path=None):
        def wrapper(handler):
            #{
            #    '/test': {
            #        'GET': handler
            #    }
            #}
            path_name = path or f"/{handler.__name__}"
            
            if path_name not in self.routes:
                self.routes[path_name] = {}

            self.routes[path_name]['GET'] = handler

            print('AQUI - - - - - - - -',self.routes)

        return wrapper