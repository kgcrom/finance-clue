from dataclasses import dataclass
from typing import Generic, List, TypeVar

T = TypeVar("T")


@dataclass
class BaseListDto(Generic[T]):
    """

    param status
    param message
    param list
    """

    status: str
    message: str
    list: List[T]
