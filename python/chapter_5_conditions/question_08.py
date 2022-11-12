#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_08():
    # -=- ANSWER START -=-
    score_a = float(input("Please enter the score of team A: "))
    score_b = float(input("Please enter the score of team B: "))
    if score_a > score_b:
        print("Team A won.")
    else:
        if score_a < score_b:
            print("Team B won.")
        else:
            print("The game is a draw.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_08]
    # Test team A win.
    tester.test(1, 0)
    # Test team B win.
    tester.test(0, 1)
    # Test draw.
    tester.test(0, 0)


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
