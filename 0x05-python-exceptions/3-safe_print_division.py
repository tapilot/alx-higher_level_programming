#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result


if __name__ == "__main__":
    dividend = 10
    divisor = 2
    division_result = safe_print_division(dividend, divisor)
