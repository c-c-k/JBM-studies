#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_extra_01():
    # -=- ANSWER START -=-
    max_num = int(input("Please enter a number: "))
    print(f"The numbers from -5 up to {max_num} are:")
    for num in range(-5, max_num):
        print(num, end=" ")
    print()


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_extra_01]
    # Test.
    tester.test(10)


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
