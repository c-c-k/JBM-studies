#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_02():
    # -=- ANSWER START -=-
    num = float(input("Please enter a number: "))
    if num.is_integer():
        num = int(num)
    if num > 0:
        num_description = "positive"
    else:
        num_description = "non positive"
    print(f"The number {num} is a {num_description} number.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_02]
    # Test positive float
    tester.test_functions(1.1)
    # Test positive integer
    tester.test_functions(1)
    # Test zero
    tester.test_functions(0)
    # Test negative number
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
