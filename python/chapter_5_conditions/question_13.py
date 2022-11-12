#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_13():
    # -=- ANSWER START -=-
    num = int(input("Please enter an integer number: "))
    if (num > 0) and (num % 2 == 0):
        print(f"The number {num} is an even positive number.")
    else:
        print(f"The number {num} is not an even positive number.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_13]
    # Test even positive.
    tester.test_functions(2)
    # Test even non-positive.
    tester.test_functions(-2)
    # Test zero.
    tester.test_functions(0)
    # Test odd positive.
    tester.test_functions(1)
    # Test odd non-positive.
    tester.test_functions(-1)


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
