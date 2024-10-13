from typing import Dict


class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        self.param = param
        self.body = body