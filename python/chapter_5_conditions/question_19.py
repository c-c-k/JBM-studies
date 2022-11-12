#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper import test_answer


# ------------------------------------------------------------
# MESSAGES
# ------------------------------------------------------------
MSG_REQ_INPUT = ("Please enter the three sides of "
                 "a triangle separated by spaces: ")


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    sides = [int(side) for side in input(MSG_REQ_INPUT).split()]
    for i in range(len(sides)):
        sum_side_lengths = sum((
            sides[j] if j != i else 0 for j in range(len(sides))))
        if sides[i] >= sum_side_lengths:
            raise ValueError


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_1(self):
        self.set_stdin("1 2 4\n")
        self.assertRaises(ValueError, main)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
