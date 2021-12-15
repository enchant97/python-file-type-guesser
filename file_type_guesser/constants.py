from . import signatures as sig
from .types import FileTypes

__all__ = [
    "FILE_SIGNATURES_WITH_EXTENTION",
    "EXTENTION_WITH_TYPE_AND_SIG",
    "EXT_ALSO_KNOWN_AS",
    "DEFAULT_SAMPLE_SIZE",
]

# known signatures (inital part of file) and their related extention
FILE_SIGNATURES_WITH_EXTENTION: dict[bytes, str] = {
    sig.SIG_JPG: "jpg",
}

EXTENTION_WITH_TYPE_AND_SIG: dict[str, tuple[FileTypes, bytes]] = {
    "jpg": (FileTypes.IMAGE, sig.SIG_JPG),
    "txt": (FileTypes.TEXT, None),
    "md": (FileTypes.TEXT, None),
}

# allows for multiple extention for one file type
EXT_ALSO_KNOWN_AS: dict[str, str] = {
    "jpe": "jpg",
    "jpeg": "jpg",
}

# size of the sample when reading from a stream
DEFAULT_SAMPLE_SIZE = 100
