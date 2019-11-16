def test_version():
    from . import __version__ as v

    assert v == "v0.0.1"
