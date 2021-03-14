import sqlite3


class SQLiteClient:

    def __init__(self, db_path: str) -> None:
        self._conn = None
        self._conn = sqlite3.connect(db_path)
        self._cur = self._conn.cursor()

    def __del__(self) -> None:
        if self._conn is not None:
            self._conn.close()

    def commit(self) -> None:
        if self._conn.isolation_level is None:
            return

        self._conn.commit()

    def execute(self, query: str, *args):
        self._cur.execute(query, *args)

    def executemany(self, query: str, *args):
        self._cur.executemany(query, *args)

    def executescript(self, query: str):
        self._cur.executescript(query)

    def fetchone(self, query: str, *args) -> tuple:
        return self._cur.execute(query, *args).fetchone()

    def fetchall(self, query: str, *args) -> list:
        return self._cur.execute(query, *args).fetchall()
