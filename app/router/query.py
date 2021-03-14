from app.application.foo import *

class QueryRouter:

    def __init__(self, foo_app: FooApplication):
        self.foo_app = foo_app

    def execute(self, value: str):
        query = value.split()
        query_type = query[0]
        query_args = query[1:]

        if query_type == "REQUEST":
            return self.__foo(*query_args)
        else:
            raise Exception(f"{query_type} is not implemented yet")

    def __foo(self, args):
        request = Request(args)
        try:
            result = self.foo_app.execute(request)
            print(result)
        except FooError:
            print("Error: Foo error")
