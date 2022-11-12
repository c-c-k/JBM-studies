#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_03():
    # -=- ANSWER START -=-
    # Get operands and operator code.
    operand_1 = float(input("Please enter the first operand: "))
    operand_2 = float(input("Please enter the second operand: "))
    operator = input("Please enter the operator code(1 for +, 2 for -): ")
    # Cast operands as integers if possible.
    if operand_1.is_integer():
        operand_1 = int(operand_1)
    if operand_2.is_integer():
        operand_2 = int(operand_2)
    # Execute the required operation according to the operator code,
    # exit if the operator code is invalid.
    if operator == "1":
        operator = "+"
        result = operand_1 + operand_2
    elif operator == "2":
        operator = "-"
        result = operand_1 - operand_2
    else:
        print("Invalid operator")
        # exit()  # uncomment if used as standalone script.
        return  # remove if used as standalone script.
    # Format and print result.
    print(f"{operand_1} {operator} {operand_2} = {result}")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_03]
    # Test bad operator
    tester.test_functions(1, 1, 0)
    # Test addition operator
    tester.test_functions(1, 1, 1)
    # Test subtraction operator
    tester.test_functions(1, 1, 2)


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
