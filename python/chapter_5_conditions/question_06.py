#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_06():
    # -=- ANSWER START -=-
    num = int(input("Please enter a number: "))
    odd_or_even = "odd" if num % 2 != 0 else "even"
    print(f"The number {num} is {odd_or_even}.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_06]
    # Test odd number.
    tester.test(1)
    # Test even number.
    tester.test(0)



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
