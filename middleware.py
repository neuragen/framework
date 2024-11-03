from starlette.middleware.base import BaseHTTPMiddleware

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Lógica do middleware (exemplo de logging)
        print(f"Requests[AQUI]: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response status[AQUI2]: {response.status_code}")
        return response
