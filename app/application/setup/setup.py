from app.repository import SQLiteClient

from .dto import *

class SetupApplication:

    def __init__(self, db: SQLiteClient):
        self.db = db

    def execute(self, request: Request) -> Response:
        pass
