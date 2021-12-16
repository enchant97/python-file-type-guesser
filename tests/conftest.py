from pathlib import Path
import pytest


@pytest.fixture(scope="session")
def data_path() -> Path:
    return Path(__file__).parent / "testdata"
