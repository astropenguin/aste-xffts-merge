# submodules
from aste_xffts_merge import __author__, __version__


# test functions
def test_author() -> None:
    assert __author__ == "Akio Taniguchi"


def test_version() -> None:
    assert __version__ == "0.1.0"
