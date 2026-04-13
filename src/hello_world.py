def hello():
    """Return a Hello World greeting message."""
    return "Hello, World!"


def greet(name):
    """Return a personalized greeting message."""
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    return f"Hello, {name.strip()}!"


def main():
    """Entry point for the application."""
    print(hello())
    print(greet("GitHub Actions"))


if __name__ == "__main__":
    main()
