from file_type_guesser.types import FileInfo


class TestFileInfoSignatureTuple:
    def test_none(self):
        file_info_none = FileInfo()
        assert len(file_info_none.signatures_as_tuple) == 0

    def test_single(self):
        file_info_single = FileInfo(signatures=b"1")
        assert len(file_info_single.signatures_as_tuple) == 1

    def test_multiple(self):
        file_info_multi = FileInfo(signatures=(b"1", b"2"))
        assert len(file_info_multi.signatures_as_tuple) == 2
