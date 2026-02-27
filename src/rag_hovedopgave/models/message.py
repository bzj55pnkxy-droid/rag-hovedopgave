from typing import Any, List

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str | None = None
    id: str | None = None
    parts: List[Any] | None = None



