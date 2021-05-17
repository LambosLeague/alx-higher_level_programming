#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    cnt = 0
    if len(my_list_1) <= len(my_list_2):
        lst = my_list_1
        my_list_1 = my_list_2
        my_list_2 = lst

    for i in my_list_1:
        try:
            result.append(my_list_2[cnt] / i)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
        cnt += 1
    return result
