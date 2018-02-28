# -*- coding=UTF-8 -*-

"""

Usually when you buy something,
you're asked whether your credit card number, phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify,
which changes all but the last four characters into '#'.

Examples : maskify("4556364607935616") == "############5616"

"""

def maskify(cc):
    a = '#'
    if len(cc) > 4:
        str_cc = a * (len(cc) - 4) + cc[-4:]
        return str_cc
    else:
        return cc

