#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_extra_03():
    # -=- ANSWER START -=-
    print("The numbers from 1 up to 20 (inclusive) that are divisible by 2 are:")
    for num in range(2, 21, 2):
        print(num, end=" ")
    print()
    print("The numbers from 1 up to 20 (inclusive) that are divisible by 3 are:")
    for num in range(3, 21, 3):
        print(num, end=" ")
    print()
    print("The numbers from 1 up to 20 (inclusive) that are divisible by 4 are:")
    for num in range(4, 21, 4):
        print(num, end=" ")
    print()


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_extra_03]
    # Test.
    tester.test_functions()


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
