from collections import defaultdict

class Request:
    def __init__(self, environ) -> None:
        self.queries = defaultdict()
        
        self.path = environ.get("path", "")
        self.method = environ.get("method", "").upper()
        self.query_string = environ.get("query_string", "")
        
        for key, val in environ.items():
            setattr(self, key.replace(".", "_").lower(), val)

        if self.query_string:
            req_queries = self.query_string.decode().split("&") if isinstance(self.query_string, bytes) else self.query_string.split("&")

            for query in req_queries:
                if "=" in query:
                    query_key, query_val = query.split("=")
                    self.queries[query_key] = query_val
