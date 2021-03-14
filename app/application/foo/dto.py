from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    value: str


@dataclass(frozen=True)
class Response:
    value: str


class FooError(Exception):...
