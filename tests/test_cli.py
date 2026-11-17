from mycli.cli import main


def test_dummy():
    # Test checks only import, does not run CLI and without builder
    assert callable(main)
