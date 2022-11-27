#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest
import diamond
import csv


def test_diamond_graded_values():
    print("--clarity and cut grade tests::")
    low_clarity = diamond.GradedValueClarity("i3")
    high_clarity = diamond.GradedValueClarity("if")
    print(f"{str(low_clarity)} < {str(high_clarity)}: ", low_clarity < high_clarity)
    low_cut = diamond.GradedValueCut("fair")
    high_cut = diamond.GradedValueCut("ideal")
    print(f"{str(low_cut)} > {str(high_cut)}: ", low_cut > high_cut)

def quicktest_answers():
    tester = QuickTest()
    with open("diamonds_test.csv", "r", newline='') as f:
        diamonds = csv.DictReader(f)


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    test_diamond_graded_values()


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
