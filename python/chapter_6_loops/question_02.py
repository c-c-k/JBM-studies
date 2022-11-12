#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_02():
    # -=- ANSWER START -=-
    from math import sqrt
    len_input = 10
    # Standard deviation formula:
    #   sqrt(sum((value - mean)**2) / number of values)
    # Mean formula:
    #   sum(values) / number of values
    sum_ = 0
    values = []
    for i in range(1, len_input + 1):
        num = float(input(f"Please enter a number ({i} of 10): "))
        values.append(num)
        sum_ += num
    mean = sum_ / len(values)
    sum_ = 0
    for value in values:
        sum_ += (value - mean) ** 2
    standard_deviation = sqrt(sum_ / len(values))
    print("The standard deviation of the entered numbers is:", standard_deviation)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    import random
    from statistics import pstdev
    tester = QuickTest()
    tester.functions = [answer_02]
    # Test standard deviation for random population.
    random.seed()
    population = [random.randint(0, 100) for _ in range(10)]
    tester.test(*population)
    print("!! The answer should be:", pstdev(population))


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
