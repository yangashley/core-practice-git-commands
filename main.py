import pytest


def always_returns_true():
    # Why does always_return_true return False?
    return False


def test_always_returns_true():
    assert always_returns_true()
