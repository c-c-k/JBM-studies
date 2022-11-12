#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_01():
    # -=- ANSWER START -=-
    sum_ = 0
    for i in range(1, 11):
        sum_ += float(input(f"Please enter a number ({i} of 10): "))
    print("The sum of the entered numbers is:", sum_)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_01]
    # Test trivial sum.
    tester.test(*(1 for _ in range(10)))


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
