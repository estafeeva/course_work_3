from utils import main
from utils import Classes

def test_read_file():
    assert len(main.read_file()) == 101


def test_main():
    assert main.main() == [None, None, None, None, None]

