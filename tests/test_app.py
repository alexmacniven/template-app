import app


def test_version():
    assert isinstance(app.__version__, str)
