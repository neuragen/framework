import os
from starlette.applications import Starlette
from starlette.middleware import Middleware
import uvicorn

class NeuraGens(Starlette):
    def __init__(self, middleware: list[Middleware] = None, **options):
        super().__init__(middleware=middleware, **options)

    def route(self, path: str, methods: list[str] = None):
        """Método para registrar rotas diretamente na aplicação."""
        return super().route(path, methods=methods)
    
    def listen(self, module_name: str = "example", port: int = 8000, host: str = "127.0.0.1", reload: bool = False, directory: str = None):
        """Inicia o servidor ASGI."""
        app_string = f"{module_name}:neuragens"
        
        if directory is None:
            uvicorn.run(app_string, host=host, port=port, reload=reload)
        else:
            uvicorn.run(app_string, host=host, port=port, reload=reload, reload_dirs=[directory])

        