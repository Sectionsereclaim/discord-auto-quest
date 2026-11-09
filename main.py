"""Entry point for service."""

from utils import prepare


def main():
    result = prepare(100)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
