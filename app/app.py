from app.application.foo import FooApplication
from app.application.setup import SetupApplication
from app.repository import SQLiteClient
from app.router import QueryRouter, SetupRouter


class App:
    _MIGRATION_FILE = "app/migration.sql"

    def __init__(self, db: SQLiteClient) -> None:
        self.db = db

        # setup
        setup_app = SetupApplication(db)
        self.setup_router = SetupRouter(setup_app)

        # query
        foo_app = FooApplication(db)
        self.query_router = QueryRouter(foo_app)

    def migration(self):
        with open(self._MIGRATION_FILE, 'r') as f:
            query = f.read()
        self.db.executescript(query)
        self.db.commit

    def setup(self, value: str):
        self.setup_router.execute(value)

    def query(self, value: str):
        self.query_router.execute(value)
