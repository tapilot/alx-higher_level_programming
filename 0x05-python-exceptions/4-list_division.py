#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for 1 in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except (ValueError, TypeError):
                result = 0
                print("wrong type")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                result_list.append(result)

    except IndexError:
        pass

    finally:
        return result_list


if __name__ == "__main__":
    list1 = [10, 20, 30, 40]
    list2 = [2, 0, 5, 10]
    length = 5
    result = list_division(list1, list2, length)
    print(result)
