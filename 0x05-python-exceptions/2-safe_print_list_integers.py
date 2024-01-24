#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    count = 0

    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=" ")
                count += 1

    except (IndexError, ValueError, TypeError):
        pass

    finally:
        print()
        return count


if __name__ == "__main__":
    my_list = [1, "two", 3, "four", 5]
    x = 4
    integers_printed = safe_print_list_integers(my_list, x)
    print(f"Number of integers printed: {integers_printed}")
