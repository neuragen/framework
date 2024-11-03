from neuragens import NeuraGens

def global_middlewares(scope):
    print('Middleware executado')

def local_middlewares(scope):
    print('Middleware local executado')

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
        teste_param = req.queries.get('nome')
        oi_param = req.queries.get('sobrenome')
        
        print(f"Parâmetro 'teste': {teste_param}")
        print(f"Parâmetro 'oi': {oi_param}")
        
        res.send(f'Parâmetros recebidos - teste: {teste_param}, oi: {oi_param}', '201')
    
    async def post(req, res):
        res.render('example', {'name': 'michael', 'message': 'Olá tudo bem?'})
    
    def hello(req, res):
        pass
