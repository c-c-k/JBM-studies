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
def get_average(n: int):
    """ Read n values from stdin input and return their average.

    :param n: The number of values to read.
    :return: The average of the n input values.
    """
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += int(input("Please enter a number to add to the sum "
                          f"({i} of {n}): "))
    return sum_ / n


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [get_average]
    # Test trivial sum.
    tester.test_functions(
        args=(10,),
        inputs=tuple(1 for _ in range(10)),
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
