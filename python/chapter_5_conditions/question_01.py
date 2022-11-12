#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_01():
    # -=- ANSWER START -=-
    num = float(input("Please enter a number: "))
    if num.is_integer():
        num = int(num)
    if num > 0:
        print(f"The number {num} is a positive number.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_01]
    # Test positive float
    tester.test(1.1)
    # Test positive integer
    tester.test(1)
    # Test zero
    tester.test(0)
    # Test negative number
    tester.test(-1)


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
