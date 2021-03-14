from app.application.foo import FooApplication
from app.application.setup import SetupApplication
from app.repository import SQLiteClient


class App:
    _MIGRATION_FILE = "app/migration.sql"

    def __init__(self, db: SQLiteClient) -> None:
        self.db = db

        # setup
        self.setup_app = SetupApplication(db)

        # foo
        self.foo_app = FooApplication(db)

    def migration(self):
        with open(self._MIGRATION_FILE, 'r') as f:
            query = f.read()
        self.db.executescript(query)
        self.db.commit

    def setup(self, value: str):
        pass

    def query(self, value: str):
        query = value.split()
        query_type = query[0]
        if query_type == "foo":
            pass
        else:
            raise Exception(f"{query_type} is not implemented yet")
