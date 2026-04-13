import pytest
from hello_world import hello, greet


class TestHelloWorld:
    """Test suite for hello_world module."""

    def test_hello_returns_greeting(self):
        assert hello() == "Hello, World!"

    def test_hello_return_type(self):
        assert isinstance(hello(), str)

    def test_greet_with_name(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_with_different_name(self):
        assert greet("GitHub Actions") == "Hello, GitHub Actions!"

    def test_greet_strips_whitespace(self):
        assert greet("  Bob  ") == "Hello, Bob!"

    def test_greet_empty_name_raises_error(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")

    def test_greet_none_raises_error(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet(None)

    def test_greet_whitespace_only_raises_error(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("   ")
