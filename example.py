#import os
from neuragens import NeuraGens, Middleware
from middleware import CustomMiddleware
from routes import setup_routes

neuragens = NeuraGens(middleware=[Middleware(CustomMiddleware)])

setup_routes(neuragens)

#current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    # , directory=current_dir - -
    neuragens.listen(module_name="example", port=3000, reload=True) 