import sys
from uuid import uuid4

from app.app import App
from app.repository import SQLiteClient


def setup() -> App:
    repo = SQLiteClient(f"app_{uuid4()}.db")
    return App(repo)

def main(lines):
    app = setup()
    m = int(lines[0])  # number of setups
    for l in lines[1:m+1]:
        app.setup(l)

    for l in lines[m+1:]:
        app.query(l)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    try:
        main(lines)
    except:
        import traceback
        traceback.print_exc()
