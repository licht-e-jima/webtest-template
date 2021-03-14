from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    value: str


@dataclass(frozen=True)
class Response:
    value: str

    def __str__(self) -> str:
        return self.value


class FooError(Exception):...
