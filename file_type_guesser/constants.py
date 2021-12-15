from . import signatures as sig
from .types import FileTypes

__all__ = [
    "EXTENTION_WITH_TYPE_AND_SIG",
    "EXT_ALSO_KNOWN_AS",
    "DEFAULT_SAMPLE_SIZE",
]

# each known extention related to their type and signature(s) if they have one
EXTENTION_WITH_TYPE_AND_SIG: dict[str, tuple[FileTypes, bytes | tuple[bytes] | None]] = {
    # images
    "bmp": (FileTypes.IMAGE, sig.SIG_BMP),
    "exr": (FileTypes.IMAGE, sig.SIG_EXR),
    "gif": (FileTypes.IMAGE, sig.SIG_GIF),
    "hdr": (FileTypes.IMAGE, sig.SIG_HDR),
    "jpg": (FileTypes.IMAGE, sig.SIG_JPG),
    "png": (FileTypes.IMAGE, sig.SIG_PNG),
    "tiff": (FileTypes.IMAGE, sig.SIG_TIFF),
    "tga": (FileTypes.IMAGE, None),
    # plain text
    "md": (FileTypes.TEXT, None),
    "txt": (FileTypes.TEXT, None),
}

# allows for multiple extention for one file type
EXT_ALSO_KNOWN_AS: dict[str, str] = {
    # images
    "jpe": "jpg",
    "jpeg": "jpg",
    "tif": "tiff",
}

# size of the sample when reading from a stream
DEFAULT_SAMPLE_SIZE = 100
