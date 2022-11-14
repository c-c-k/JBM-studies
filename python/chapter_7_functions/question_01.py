#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_01():
    # -=- ANSWER START -=-
    num = int(input("Please enter a number: "))
    odd_or_even = "odd" if is_odd(num) else "even"
    print(f"The number {num} is {odd_or_even}.")


def is_odd(num: int) -> int:
    return num % 2


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_01]
    # Test odd number.
    tester.test_functions(inputs=(1,),)
    # Test even number.
    tester.test_functions(inputs=(0,),)


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
