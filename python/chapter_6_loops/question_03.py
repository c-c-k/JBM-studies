#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_03():
    # -=- ANSWER START -=-
    num = float(input(f"Please enter a number (enter 0 to exit): "))
    min_, max_ = num, num
    while num:
        if num < min_:
            min_ = num
        if num > max_:
            max_ = num
        num = float(input(f"Please enter a number (enter 0 to exit): "))
    print("The minimum of the entered numbers is:", min_)
    print("The maximum of the entered numbers is:", max_)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_03]
    # Test trivial population.
    tester.test(*range(1, 6), *range(-5, 1))


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
