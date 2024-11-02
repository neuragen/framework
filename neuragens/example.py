from neuragens.main import NeuraGens

def global_middlewares(scope):
    print('Middleware executed')

def local_middlewares(scope):
    print('Local Middleware executed')

neuragens = NeuraGens(middlewares=[global_middlewares])

@neuragens.get('/name/{id}/{color}', middlewares=[local_middlewares])
async def get_test(req, res, id, color):
    res.send(f"['id', '{id}', 'color', '{color}']", '201 OK')

@neuragens.post('/name')
def post_name(req, res):
    res.send('OLA TUDO BEM', '201')


@neuragens.route("/users", middlewares=[local_middlewares])
class User:
    def __init__(self):
        pass
    async def get(req, res):
        res.send('OLA TUDO BEM', '201')
    
    async def post(req, res):
        res.send('POST - OLA TUDO BEM', '201')
    
    def hello(req, res):
        pass