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
MAX_INPUTS = 10

# ------------------------------------------------------------
# MESSAGES
# ------------------------------------------------------------
MSG_REQ_INPUT = "Please enter a number ({CURRENT} of {MAX}): "
MSG_BAD_INPUT = "Float or integer values only."
MSG_OUTPUT = "The sum of the {INPUTS} input numbers is: {SUM}"


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    sum_ = 0
    current_input = 1
    while current_input <= MAX_INPUTS:
        try:
            num = float(input(MSG_REQ_INPUT.format(CURRENT=current_input, MAX=MAX_INPUTS)))
        except ValueError:
            print(MSG_BAD_INPUT)
            continue
        sum_ += num
        current_input += 1
    print(MSG_OUTPUT.format(INPUTS=MAX_INPUTS, SUM=sum_))


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
def test_main():
    tester = test_answer.ManualTest(test_func=main)
    tester.test_input(*[1 for _ in range(10)])


class TestAnswer(test_answer.TestAnswer):
    pass


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    # test_answer.unittest.main()
    # main()
    test_main()
