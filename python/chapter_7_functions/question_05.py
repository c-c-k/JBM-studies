#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_02():
    pass


# -=- ANSWER START -=-
def power(base: float | int, exponent: int):
    """Return base to the power of exponent.

    Fractional exponents are not handled.
    :param base: The base of the power expression.
    :param exponent: The exponent of the power expression.
    :return: base taken to the power of exponent.
    """
    if exponent == 0:
        return 1
    result = base
    negative_exponent = exponent < 0
    exponent = abs(exponent)
    for _ in range(exponent - 1):
        result *= base
    if negative_exponent:
        result = 1 / result
    return result


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [power]
    # Test exponent 0.
    tester.test_functions(
        args=(2, 0,),
        print_return=True,
    )
    # Test exponent 1.
    tester.test_functions(
        args=(2, 1,),
        print_return=True,
    )
    # Test exponent -2.
    tester.test_functions(
        args=(2, -2,),
        print_return=True,
    )


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    pass


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    quicktest_answers()
    # main()
# -=- TEST END -=-
