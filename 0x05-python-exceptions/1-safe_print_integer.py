#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    result1 = safe_print_integer(42)
    result2 = safe_print_integer("Hello")

    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
