from io import BufferedReader
from pathlib import Path

from .constants import (DEFAULT_SAMPLE_SIZE, EXT_ALSO_KNOWN_AS,
                        EXTENTION_WITH_TYPE_AND_SIG)
from .types import ContentGuess, FileTypes


def check_if_text(stream: BufferedReader, sample_size: int) -> bool:
    try:
        sample = stream.read(sample_size)
        sample.decode()
    except UnicodeDecodeError:
        return False
    return True


def check_signature_match(stream: BufferedReader, *signatures: bytes) -> bool:
    if len(signatures) == 0:
        return False

    stream.seek(0)

    for sig in signatures:
        sig_len = len(sig)
        read = stream.read(sig_len)
        stream.seek(0)

        if len(read) == sig_len:
            if sig == read:
                return True
    return False


def guess_file(file_path: Path) -> ContentGuess:
    category = FileTypes.BINARY
    ext = file_path.suffix.lower().removeprefix(".")
    type_and_sig = EXTENTION_WITH_TYPE_AND_SIG.get(ext, None)
    if type_and_sig is None:
        actual_ext = EXT_ALSO_KNOWN_AS.get(ext, None)
        if actual_ext:
            ext = actual_ext
            type_and_sig = EXTENTION_WITH_TYPE_AND_SIG.get(ext, None)
    content_ext = None

    if type_and_sig is not None:
        type_, sig = type_and_sig

        if sig:
            # has a signature, so check that
            with open(file_path, "rb") as fo:
                if not isinstance(sig, tuple):
                    sig = (sig,)
                if check_signature_match(fo, *sig):
                    content_ext = ext
                    category = type_
        else:
            # has no signature
            is_text = None
            with open(file_path, "rb") as fo:
                is_text = check_if_text(fo, DEFAULT_SAMPLE_SIZE)
            if ((type_ == FileTypes.TEXT and is_text is True) or
                    (type_ != FileTypes.TEXT and is_text is False)):
                content_ext = ext
                category = type_

    return ContentGuess(category, ext, content_ext)
