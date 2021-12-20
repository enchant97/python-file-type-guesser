from . import signatures as sig
from .types import FileInfo, FileTypes

__all__ = [
    "DEFAULT_SAMPLE_SIZE",
    "EXT_ALSO_KNOWN_AS",
    "EXTENTION_WITH_FILE_INFO",
]

# size of the sample when reading from a stream
DEFAULT_SAMPLE_SIZE = 100

# allows for multiple extention for one file type
EXT_ALSO_KNOWN_AS: dict[str, str] = {
    # images
    "jpe": "jpg",
    "jpeg": "jpg",
    "tif": "tiff",
    # videos
    "mpeg": "mpg",
    "vob": "mpg",
    "webm": "mkv",
}

# each known extention related to their file info
EXTENTION_WITH_FILE_INFO: dict[str, FileInfo] = {
    # images
    "bmp": FileInfo(FileTypes.IMAGE, sig.SIG_BMP),
    "exr": FileInfo(FileTypes.IMAGE, sig.SIG_EXR),
    "gif": FileInfo(FileTypes.IMAGE, sig.SIG_GIF),
    "hdr": FileInfo(FileTypes.IMAGE, sig.SIG_HDR),
    "jpg": FileInfo(FileTypes.IMAGE, sig.SIG_JPG),
    "png": FileInfo(FileTypes.IMAGE, sig.SIG_PNG),
    "tiff": FileInfo(FileTypes.IMAGE, sig.SIG_TIFF),
    "tga": FileInfo(FileTypes.IMAGE),
    # video
    "mov": FileInfo(FileTypes.VIDEO, sig.SIG_MOV, 4),
    "mp4": FileInfo(FileTypes.VIDEO, sig.SIG_MP4, 4),
    "mpg": FileInfo(FileTypes.VIDEO, sig.SIG_MPG),
    "mkv": FileInfo(FileTypes.VIDEO, sig.SIG_MKV),
    # plain text
    "md": FileInfo(FileTypes.TEXT),
    "txt": FileInfo(FileTypes.TEXT),
}
