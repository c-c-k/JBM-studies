#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_03():
    # -=- ANSWER START -=-
    while True:
        num = int(input("Please enter an integer value (-999 to exit): "))
        if num == -999:
            break
        print(f"The number of digits in {num} is {num_digits(num)}.")


def num_digits(num: int) -> int:
    """Count the number of digits in the input number.

    :param num: The number for which the digits are to be counted.
    :return: The number of digits in num.
    """
    return len(str(abs(num)))


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_03]
    # Test.
    tester.test_functions(inputs=(1, -22, -12345, -999), )


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
