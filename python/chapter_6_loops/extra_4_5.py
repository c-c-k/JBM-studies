#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper import test_answer

# ------------------------------------------------------------
# CONSTANTS
# ------------------------------------------------------------

# ------------------------------------------------------------
# MESSAGES
# ------------------------------------------------------------
MSG_REQ_INPUT = "Please enter the top number up to which to count: "
MSG_OUTPUT = "The sum of the numbers up to {NUM} is: {SUM}"


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    top_num = input(MSG_REQ_INPUT)
    num = top_num
    sum_ = 0
    while num:
        sum_ += num
        num -= 1
    print(MSG_OUTPUT.format(NUM=top_num, SUM=sum_))


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
def test_main():
    pass


class TestAnswer(test_answer.TestAnswer):
    pass


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    # test_answer.unittest.main()
    main()
    # test_main()

