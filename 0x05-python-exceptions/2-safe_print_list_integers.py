#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        try:
            if my_list[i] % my_list[i] == 0:
                print("{:d}".format(my_list[i]), end="")
                cnt += 1
        except TypeError:
            pass
    print(end="\n")
    return cnt
