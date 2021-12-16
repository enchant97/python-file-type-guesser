from io import BufferedReader
from pathlib import Path
from typing import Optional

from .constants import (DEFAULT_SAMPLE_SIZE, EXT_ALSO_KNOWN_AS,
                        EXTENTION_WITH_FILE_INFO)
from .types import ContentGuess, FileInfo, FileTypes

__all__ = [
    "check_if_text", "check_signature_match",
    "find_file_info", "guess",
    "guess_file", "guess_stream",
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


def check_signature_match(stream: BufferedReader, file_info: FileInfo) -> bool:
    """
    Check whether a stream matches given signatures

        :param stream: The stream
        :param file_info: The files info to match to
        :return: Whether it matched
    """
    if len(file_info.signatures_as_tuple) == 0:
        return True

    stream.seek(0)

    for sig in file_info.signatures_as_tuple:
        sig_len = len(sig)
        if file_info.bytes_offset:
            # move to offset before read
            stream.seek(file_info.bytes_offset)
        read = stream.read(sig_len)
        stream.seek(0)

        if len(read) == sig_len:
            if sig == read:
                return True
    return False


def find_file_info(ext: str) -> tuple[str, FileInfo]:
    """
    Get the extention and file type
    info for the given extention

        :param ext: The files extention
        :return: the recognised extention and file type info
    """
    file_type_info = EXTENTION_WITH_FILE_INFO.get(ext, None)
    if file_type_info is None:
        actual_ext = EXT_ALSO_KNOWN_AS.get(ext, None)
        if actual_ext:
            ext = actual_ext
            file_type_info = EXTENTION_WITH_FILE_INFO.get(ext, None)
    return ext, file_type_info


def guess(file_path: Path | str, stream: Optional[BufferedReader] = None) -> ContentGuess:
    """
    Make a guess with given file, using given stream for content if provided

        :param file_path: The filepath of stream
        :param stream: A stream to use, defaults to None
        :return: The content guess
    """
    if isinstance(file_path, str):
        # allow for strings to be passed in
        file_path = Path(file_path)

    category = FileTypes.BINARY
    ext = file_path.suffix.lower().removeprefix(".")
    content_ext = None
    ext, file_type_info = find_file_info(ext)

    if file_type_info is not None:
        # a recogised file type
        if file_type_info.signatures is not None:
            # has a signature, so check that
            with stream if stream is not None else open(file_path, "rb") as fo:
                if check_signature_match(fo, file_type_info):
                    content_ext = ext
                    category = file_type_info.type_
        else:
            # has no signature
            is_text = None
            with stream if stream is not None else open(file_path, "rb") as fo:
                is_text = check_if_text(fo, DEFAULT_SAMPLE_SIZE)
            if ((file_type_info.type_ == FileTypes.TEXT and is_text is True) or
                    (file_type_info.type_ != FileTypes.TEXT and is_text is False)):
                content_ext = ext
                category = file_type_info.type_

    return ContentGuess(category, ext, content_ext)


def guess_file(file_path: Path) -> ContentGuess:  # pragma: no cover
    """
    Make a guess of file type with given file path

        :param file_path: The filepath of file
        :return: The content guess
    """
    return guess(file_path)


def guess_stream(file_path: Path, stream: BufferedReader) -> ContentGuess:  # pragma: no cover
    """
    Make a guess with given file, using given stream for content

        :param file_path: The filepath of stream
        :param stream: A stream to use
        :return: The content guess
    """
    return guess(file_path, stream)
