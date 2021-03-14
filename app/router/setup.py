from app.application.setup import SetupApplication, Request, Response


class SetupRouter:
    def __init__(self, setup_app: SetupApplication):
        self.setup_app = setup_app

    def execute(self, value: str):
        request: Request = Request(value)
        result = self.setup_app.execute(request)
        print(result)
