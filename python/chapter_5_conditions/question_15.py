#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_15():
    # -=- ANSWER START -=-
    num = int(input("Please enter an integer number: "))
    if 9 < abs(num) < 100:
        print(f"The number {num} is a two digit number.")
    else:
        print(f"The number {num} is not a two digit number.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_15]
    # Test two digit positive.
    tester.test(42)
    # Test two digit negative.
    tester.test(-23)
    # Test single digit.
    tester.test(-2)
    # Test 3+ digits.
    tester.test(123)


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
