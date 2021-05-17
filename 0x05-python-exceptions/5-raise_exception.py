#!/usr/bin/python3
def raise_exception():
    x = "holberton!"
    if type(x) is not int:
        raise TypeError("holbeton! is string")
