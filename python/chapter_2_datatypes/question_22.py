#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.tests import test_answer

COLOR_1_PRICE = 10
COLOR_2_PRICE = 20
COLOR_3_PRICE = 30
COLOR_4_PRICE = 40
COLOR_1_NAME = "color_1"
COLOR_2_NAME = "color_2"
COLOR_3_NAME = "color_3"
COLOR_4_NAME = "color_4"


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    color_1_qty = input("Enter quantity of " + COLOR_1_NAME + " to buy: ")
    color_2_qty = input("Enter quantity of " + COLOR_2_NAME + " to buy: ")
    color_3_qty = input("Enter quantity of " + COLOR_3_NAME + " to buy: ")
    color_4_qty = input("Enter quantity of " + COLOR_4_NAME + " to buy: ")
    color_1_total_cost = int(color_1_qty) * COLOR_1_PRICE
    color_2_total_cost = int(color_2_qty) * COLOR_2_PRICE
    color_3_total_cost = int(color_3_qty) * COLOR_3_PRICE
    color_4_total_cost = int(color_4_qty) * COLOR_4_PRICE
    total_cost = (
            color_1_total_cost + color_2_total_cost
            + color_3_total_cost + color_4_total_cost
    )
    print("The total cost for all colors is:", total_cost)


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_int(self):
        self.set_stdin("1\n1\n1\n1\n")
        self.expected_output = (
            "Enter quantity of color_1 to buy: "
            "Enter quantity of color_2 to buy: "
            "Enter quantity of color_3 to buy: "
            "Enter quantity of color_4 to buy: "
            "The total cost for all colors is: 100\n"
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
