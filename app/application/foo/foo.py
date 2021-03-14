from app.repository import SQLiteClient

from .dto import *


class FooApplication:

    def __init__(self, db: SQLiteClient):
        self.db = db

    def execute(self, request: Request) -> Response:
        pass
