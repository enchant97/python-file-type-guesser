from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Optional


class FileTypes(IntEnum):
    # plain-text type
    TEXT = auto()
    # any file not recognised
    BINARY = auto()
    IMAGE = auto()
    VIDEO = auto()
    AUDIO = auto()


@dataclass
class ContentGuess:
    category: FileTypes
    extention: Optional[str] = None
    content_ext: Optional[str] = None
