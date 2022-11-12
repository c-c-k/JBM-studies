#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_05():
    # -=- ANSWER START -=-
    num = float(input("Please enter a number: "))
    num_abs = num if num >= 0 else -1 * num
    print(f"The absolute value of the number {num} is {num_abs}")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_05]
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
