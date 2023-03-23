import pytest


def always_returns_true():
    # Addsing some descriptive comment
    return False


def test_always_returns_true():
    assert always_returns_true()
