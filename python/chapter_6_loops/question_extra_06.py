#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_extra_06():
    # -=- ANSWER START -=-
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    for name in (first_name, last_name):
        z_flag = False
        for letter in name:
            if letter == "Z":
                z_flag = True
                break
        if z_flag:
            print("ZZZ")
            break
    else:
        print(first_name, last_name)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_extra_06]
    # Test no Z full name.
    tester.test("FirstName", "LastName")
    # Test Z first name.
    tester.test("FirstZName", "LastName")
    # Test Z last name.
    tester.test("FirstZName", "LastZName")


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
