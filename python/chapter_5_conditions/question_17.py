#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_17():
    # -=- ANSWER START -=-
    years = int(input("Please enter the number of years that the driver has been paying insurance: "))
    claims = int(input("Please enter the number of times the driver claimed pay out: "))
    base_premium = int(input("Please enter the drivers base premium payment: "))
    if (years > 5) or (claims <= 10):
        premium = base_premium * 0.85
    else:
        premium = base_premium
    print("The drivers premium payment is:", premium)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_17]
    # Test years > 5 , claims <= 10
    tester.test_functions(6, 9, 1000)
    # Test years > 5 , claims > 10
    tester.test_functions(6, 19, 1000)
    # Test years < 5 , claims <= 10
    tester.test_functions(3, 9, 1000)
    # Test years < 5 , claims > 10
    tester.test_functions(3, 19, 1000)


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
