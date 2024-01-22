#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1

    except IndexError:
        pass

    finally:
        print()
        return count


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    x = 3
    elements_printed = safe_print_list(my_list, x)
    print(f"Number of elements printed: {elements_printed}")
