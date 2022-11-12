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
    name = input("Enter the name: ")
    base_pay = float(input("Enter the monthly pay: "))
    additions = float(input("Enter the sum of the additions: "))
    net_pay = round(base_pay * 0.9 + additions, 1)
    print(name, "'s salary is: ", net_pay, sep="")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_int(self):
        self.set_stdin("Lavit\n5000\n200")
        self.expected_output = (
            "Enter the name: "
            "Enter the monthly pay: "
            "Enter the sum of the additions: "
            "Lavit's salary is: 4700.0\n"
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
