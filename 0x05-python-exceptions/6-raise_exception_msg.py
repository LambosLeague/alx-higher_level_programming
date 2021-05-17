#!/usr/bin/python3
def raise_exception_msg(message=""):
    x = "holberton!"
    if type(x) is not int:
        raise NameError(message)
