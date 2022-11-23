#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest
from diamond import Diamond, DiamondList
import csv


# -=- ANSWER START -=-
def answer_01():
    pass


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_01]
    # diamond = Diamond(0.23, "Ideal", "E", "SI2", 61.5, 55.0, 326, 3.95, 3.98, 2.43)
    diamond_list = DiamondList()
    with open("diamonds_test.csv", "r", newline='') as f:
        diamonds = csv.DictReader(f)
        for diamond in diamonds:
            diamond_list.add(Diamond(**diamond))
    print(*diamond_list.get_all(), sep="\n")

    # with open("diamonds.csv", "r", newline='') as f:
    #     diamonds = csv.DictReader(f)
    #     cut_names = set()
    #     for diamond in diamonds:
    #         cut_names.add(diamond["clarity"])
    # print(cut_names)


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
