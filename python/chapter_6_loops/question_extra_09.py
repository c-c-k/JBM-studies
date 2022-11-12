#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_extra_09():
    # -=- ANSWER START -=-
    first_num = 100
    last_num = 999
    divisor = 5
    print(f"The numbers from {first_num} up to {last_num} (inclusive) that are divisible by {divisor} are:")
    while first_num % divisor:
        first_num += 1
    count = 0
    for num in range(first_num, last_num + 1, divisor):
        count += 1
        print(num, end=" ")
    print()
    print("The count of the above numbers is:", count)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_extra_09]
    # Test.
    tester.test()


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
