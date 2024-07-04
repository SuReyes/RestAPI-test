from pydantic import BaseModel


class Poem(BaseModel):
    title: str
    author: str
    lines: list[str]
    linecount: int
