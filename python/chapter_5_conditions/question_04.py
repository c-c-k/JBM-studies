#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_04():
    # -=- ANSWER START -=-
    # Get first name, last name and male supremacist gender.
    first_name = input("WHAT .. is your first name: ")
    last_name = input("WHAT .. is your last name: ")
    is_supremacist_male = input("are you a real man(y/n): ")
    # Choose gender title.
    if is_supremacist_male in "yY":
        gender_title = "Mr."
    else:
        gender_title = "Mrs."
    # Format and print result.
    print(
        f"Hello, {gender_title} {first_name} {last_name}"
        ", NIce To Meet You."
    )


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_04]
    # Test real man
    tester.test("FirstName", "LastName", "Y")
    # Test lumberjack
    tester.test("FirstName", "LastName", "You misogynist pigs.")


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
