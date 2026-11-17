from mycli.cli import start

def test_dummy():
    # Test checks only import, does not run CLI and without builder
    assert callable(start)
