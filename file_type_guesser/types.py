from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Optional

__all__ = [
    "FileTypes", "ContentGuess",
    "FileInfo",
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
    DOCUMENT = auto()


@dataclass
class ContentGuess:
    """
    A files guessed content type
    """
    category: FileTypes
    extention: Optional[str] = None
    content_ext: Optional[str] = None


@dataclass
class FileInfo:
    """
    A file types info
    """
    type_: FileTypes = FileTypes.BINARY
    signatures: Optional[bytes | tuple[bytes]] = None
    bytes_offset: int = 0

    @property
    def signatures_as_tuple(self) -> tuple[bytes]:
        if self.signatures is None:
            return tuple()
        elif not isinstance(self.signatures, tuple):
            return (self.signatures,)
        return self.signatures
