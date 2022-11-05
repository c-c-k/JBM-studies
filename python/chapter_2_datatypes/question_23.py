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
    print("This program solves a system of two linear equations")
    a1, b1, c1 = input(
        "Enter the coefficients of the first equation (a1, b1, c1) : ").split()
    a1, b1, c1 = int(a1), int(b1), int(c1)
    a2, b2, c2 = input(
        "Enter the coefficients of the first equation (a2, b2, c2) : ").split()
    a2, b2, c2 = int(a2), int(b2), int(c2)
    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
    print("The solution is: ", "x=", x, " y=", y, sep="")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_int(self):
        self.set_stdin("2 3 5\n6 4 10\n")
        self.expected_output = (
            "This program solves a system of two linear equations\n"
            "Enter the coefficients of the first equation (a1, b1, c1) : "
            "Enter the coefficients of the first equation (a2, b2, c2) : "
            "The solution is: x=1.0 y=1.0\n"
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
