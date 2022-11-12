#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_07():
    # -=- ANSWER START -=-
    num = float(input("Please enter a number: "))
    if num > 0:
        num_description = "a positive number"
    else:
        if num < 0:
            num_description = "a negative number"
        else:
            num_description = "zero"
    print(f"The number {num} is {num_description}.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_07]
    # Test positive number.
    tester.test(1)
    # Test zero.
    tester.test(0)
    # Test negative number.
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
