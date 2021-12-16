from io import BytesIO
from pathlib import Path

from file_type_guesser import core
from file_type_guesser.constants import (DEFAULT_SAMPLE_SIZE,
                                         EXTENTION_WITH_FILE_INFO)
from file_type_guesser.types import FileTypes


class TestCheckIfText():
    def test_text(self):
        with BytesIO(b"hello") as stream:
            assert core.check_if_text(stream, DEFAULT_SAMPLE_SIZE)

    def test_binary(self):
        with BytesIO(b"\x02\xFF\x4A") as stream:
            assert not core.check_if_text(stream, DEFAULT_SAMPLE_SIZE)


class TestCheckSignatureMatch:
    def test_png(self, data_path: Path):
        with open(data_path / "test.png", "rb") as stream:
            file_info = EXTENTION_WITH_FILE_INFO["png"]
            assert core.check_signature_match(stream, file_info)

    def test_png_invalid(self, data_path: Path):
        with open(data_path / "test.png", "rb") as stream:
            file_info = EXTENTION_WITH_FILE_INFO["jpg"]
            assert not core.check_signature_match(stream, file_info)

    def test_txt(self, data_path: Path):
        with open(data_path / "test.txt", "rb") as stream:
            file_info = EXTENTION_WITH_FILE_INFO["txt"]
            assert core.check_signature_match(stream, file_info)

    def test_mp4(self, data_path: Path):
        with open(data_path / "test.mp4", "rb") as stream:
            file_info = EXTENTION_WITH_FILE_INFO["mp4"]
            assert core.check_signature_match(stream, file_info)


class TestFindFileInfo:
    def test_txt(self):
        ext_valid = "txt"
        assert core.find_file_info(ext_valid)[1].type_ is FileTypes.TEXT

    def test_known(self):
        ext_valid_also_known = "jpeg"
        assert core.find_file_info(ext_valid_also_known)[1].type_ is FileTypes.IMAGE

    def test_invalid(self):
        ext_invalid = "test"
        assert core.find_file_info(ext_invalid)[1] is None


class TestGuessFile:
    def test_jpg(self, data_path: Path):
        file_path_binary = data_path / "test.jpg"
        assert core.guess(file_path_binary).content_ext == "jpg"

    def test_txt(self, data_path: Path):
        file_path_text = data_path / "test.txt"
        assert core.guess(file_path_text).content_ext == "txt"

    def test_invalid_bin(self, data_path: Path):
        file_path_invalid_bin = data_path / "test.invalid-bin"
        assert core.guess(file_path_invalid_bin).content_ext is None

    def test_invalid_jpg(self, data_path: Path):
        file_path_invalid_jpg = data_path / "test.invalid.jpg"
        assert core.guess(file_path_invalid_jpg).content_ext is None

    def test_str_path(self, data_path: Path):
        file_path_text_str = str(data_path / "test.txt")
        assert core.guess(file_path_text_str).content_ext == "txt"
