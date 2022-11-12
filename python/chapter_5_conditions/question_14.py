#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_14():
    # -=- ANSWER START -=-
    num = float(input("Please enter a real number: "))
    if 0 <= num <= 1:
        print(f"The number {num} is a proper fraction.")
    else:
        print(f"The number {num} is not a proper fraction.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_14]
    # Test zero.
    tester.test_functions(0)
    # Test one.
    tester.test_functions(1)
    # Test proper fraction.
    tester.test_functions(0.2)
    # Test non-proper fraction bigger than 1.
    tester.test_functions(2)
    # Test non-proper fraction smaller than 0.
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
