from neuragens import NeuraGens, Request, Response
from starlette.responses import JSONResponse

def setup_routes(neuragens: NeuraGens):
    @neuragens.route("/api/hello", methods=["GET"])
    async def hello(request: Request) -> Response:
        return JSONResponse({"message": "Hello, World 123!"})
    
    @neuragens.route("/api/hellos", methods=["GET"])
    async def hellos(request: Request) -> Response:
        name = request.query_params.get("name", "World")
        world = request.query_params.get("World", "123")

        return JSONResponse({"message": f"Hello, {name} and {world}!"})
    
    @neuragens.route("/api/{nome}", methods=["GET"])
    async def nome(request: Request) -> Response:
        nome = request.path_params["nome"]
        return JSONResponse({"message": f"Hello, {nome}!"})
    
    @neuragens.route("/api/data", methods=["POST"])
    async def receive_data(request: Request) -> Response:
        data = await request.json()
        return JSONResponse({"received": data, 'error': False})
        
