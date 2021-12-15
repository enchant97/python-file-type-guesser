from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Optional

__all__ = [
    "FileTypes", "ContentGuess",
]


class FileTypes(IntEnum):
    """
    A files type
    """
    # plain-text type
    TEXT = auto()
    # any file not recognised
    BINARY = auto()
    IMAGE = auto()
    VIDEO = auto()
    AUDIO = auto()


@dataclass
class ContentGuess:
    """
    A files guessed content type
    """
    category: FileTypes
    extention: Optional[str] = None
    content_ext: Optional[str] = None
