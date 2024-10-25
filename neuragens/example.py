from neuragens.main import NeuraGens

neuragens = NeuraGens()

@neuragens.get('/name/{id}/{color}')
def get_test(req, res, id, color):
    res.send(f"['id', '{id}', 'color', '{color}']", '200 OK')

@neuragens.post('/name')
def post_name(req, res):
    res.send('OLA TUDO BEM', '201')