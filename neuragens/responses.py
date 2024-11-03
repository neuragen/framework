import re


class Response:
    def __init__(self, status_code="404 Not Found", text="Route not found!") -> None:
        self.status_code = status_code
        self.text = text
        self.headers = []

    def as_wsgi(self, start_response):
        start_response(self.status_code, headers=self.headers)
        return [self.text.encode()]

    async def as_asgi(self, send):
        # Envia o início da resposta com o status e cabeçalhos
        await send({
            "type": "http.response.start",
            "status": int(self.status_code.split()[0]),  # Extrai o código de status como um número
            "headers": [(key.encode("utf-8"), value.encode("utf-8")) for key, value in self.headers]
        })

        # Envia o corpo da resposta
        await send({
            "type": "http.response.body",
            "body": self.text.encode("utf-8"),
        })

    def send(self, text="", status_code="200 OK"):
        if isinstance(text, str):
            self.text = text
        else:
            self.text = str(text)

        if isinstance(status_code, int):
            self.status_code = f"{status_code} OK" if status_code == 200 else str(status_code)
        elif isinstance(status_code, str):
            self.status_code = status_code
        else:
            raise ValueError("Status code has to be either an integer or string")
    
    def render(self, template_name, context={}):
        path = f"{template_name}.html"

        with open(path) as fp:
            template = fp.read()

            for key, value in context.items():
                template = re.sub(r'{{\s*' + re.escape(key) + r'\s*}}', str(value), template)
        
        self.headers.append(('Content-Type', "text/html"))
        self.text = template
        self.status_code = "200 OK"