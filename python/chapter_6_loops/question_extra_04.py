#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_extra_04():
    # -=- ANSWER START -=-
    while True:
        max_num = int(input("Please enter a positive number (-1 to exit): "))
        if max_num == -1:
            break
        elif max_num <= 0:
            continue
        sum_ = 0
        for num in range(1, max_num + 1):
            sum_ += num
        print(f"The sum of the numbers from 1 up to {max_num} is: {sum_}")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_extra_04]
    # Test.
    tester.test_functions(*range(11), -1)


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
