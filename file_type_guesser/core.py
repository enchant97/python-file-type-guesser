from io import BufferedReader
from pathlib import Path
from typing import Optional

from .constants import (DEFAULT_SAMPLE_SIZE, EXT_ALSO_KNOWN_AS,
                        EXTENTION_WITH_TYPE_AND_SIG)
from .types import ContentGuess, FileTypes

__all__ = [
    "check_if_text", "check_signature_match",
    "guess", "guess_file", "guess_stream",
]


def check_if_text(stream: BufferedReader, sample_size: int) -> bool:
    """
    Check whether a stream is a plain-text file

        :param stream: The stream
        :param sample_size: the sample size that is checked
        :return: Whether stream is plain-text
    """
    try:
        stream.seek(0)
        sample = stream.read(sample_size)
        sample.decode()
        stream.seek(0)
    except UnicodeDecodeError:
        return False
    return True


def check_signature_match(stream: BufferedReader, *signatures: bytes) -> bool:
    """
    Check whether a stream matches given signatures

        :param stream: The stream
        :return: Whether a signature has matched
    """
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


def guess(file_path: Path, stream: Optional[BufferedReader] = None) -> ContentGuess:
    """
    Make a guess with given file, using given stream for content if provided

        :param file_path: The filepath of stream
        :param stream: A stream to use, defaults to None
        :return: The content guess
    """
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
            with stream if stream is not None else open(file_path, "rb") as fo:
                if not isinstance(sig, tuple):
                    sig = (sig,)
                if check_signature_match(fo, *sig):
                    content_ext = ext
                    category = type_

        else:
            # has no signature
            is_text = None
            with stream if stream is not None else open(file_path, "rb") as fo:
                is_text = check_if_text(fo, DEFAULT_SAMPLE_SIZE)
            if ((type_ == FileTypes.TEXT and is_text is True) or
                    (type_ != FileTypes.TEXT and is_text is False)):
                content_ext = ext
                category = type_

    return ContentGuess(category, ext, content_ext)


def guess_file(file_path: Path) -> ContentGuess:
    """
    Make a guess of file type with given file path

        :param file_path: The filepath of file
        :return: The content guess
    """
    return guess(file_path)


def guess_stream(file_path: Path, stream: BufferedReader) -> ContentGuess:
    """
    Make a guess with given file, using given stream for content

        :param file_path: The filepath of stream
        :param stream: A stream to use
        :return: The content guess
    """
    return guess(file_path, stream)
