from typing import Any, List

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str | None = None
    id: str | None = None
    parts: List[Any] | None = None


# =============================================================================
# EXAMPLE: Union type hints for multiple allowed types
# =============================================================================
# from typing import Union
#
# # This field can be a string, an int, or None:
# flexible_field: Union[str, int, None] = None
#
# # Modern Python 3.10+ shorthand using pipe:
# flexible_field: str | int | None = None
#
# # Optional[str] is equivalent to:
# content: Union[str, None] = None
# content: str | None = None  # same thing in 3.10+
# =============================================================================
