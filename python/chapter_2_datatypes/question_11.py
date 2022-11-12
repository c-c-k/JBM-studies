#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper import test_answer


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    num = int(input())
    sum_ = num
    num = int(input())
    sum_ += num
    num = int(input())
    sum_ -= num
    num = int(input())
    sum_ *= num
    num = int(input())
    sum_ //= num
    print(sum_)


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):
    test_input = "7\n7\n4\n4\n5\n"
    expected_output = "8\n"

    def test_answer(self):
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
