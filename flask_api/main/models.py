import typing


class Response(typing.TypedDict):
    search_text: str
    links: list


class Metrics(typing.TypedDict):
    search_text: list
    response_time: float
