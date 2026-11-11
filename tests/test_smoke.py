import sys


def test_python_version():
    assert sys.version_info >= (3, 10)


def test_running_inside_venv():
    assert ".venv" in sys.prefix