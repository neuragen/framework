class Response:
    def __init__(self, status_code="404 Missing Not Found", text="Route not found!") -> None:
        self.status_code = status_code
        self.text = text
        self.headers = []

    def as_wsgi(self, start_response):
        start_response(self.status_code, headers=self.headers)

    def send(self, text="", status_code="200 OK"):
        if isinstance(text, str):
            self.text = text
        else:
            self.text = str(text)
        self.status_code = status_code
