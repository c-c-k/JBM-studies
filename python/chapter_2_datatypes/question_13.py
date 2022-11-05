#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.tests import test_answer


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    num = float(input("Enter a number: \n"))
    if int(num) == num:
        num = int(num)
        sqr = num ** 2
    else:
        sqr = round(num ** 2, 3)
    print("The square of", num, "is", sqr, sep=" ")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_float(self):
        self.set_stdin("0.1\n")
        self.expected_output = (
            "Enter a number: \n"
            "The square of 0.1 is 0.01\n"
        )
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)

    def test_answer_int(self):
        self.set_stdin("10\n")
        self.expected_output = (
            "Enter a number: \n"
            "The square of 10 is 100\n"
        )
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
