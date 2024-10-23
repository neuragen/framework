from neuragens.main import NeuraGens

neuragens = NeuraGens()

@neuragens.get('/name')
def get_test(req, res):
    res.send("['michael 1234', 'douglas']", '200 OK')
