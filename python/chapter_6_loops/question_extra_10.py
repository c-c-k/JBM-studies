#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_extra_10():
    # -=- ANSWER START -=-
    email_address = input("Please enter an email address for format validation: ")
    valid_address = True
    has_at_separator = False
    for char in email_address[1:-1]:
        if char == "@":
            if has_at_separator:
                valid_address = False
                print("Email Address contains multiple @ separators.")
                break
            else:
                has_at_separator = True
    else:
        if not has_at_separator:
            valid_address = False
            print("Email Address does not contain a valid @ separator.")
    for char in email_address:
        if char == " ":
            valid_address = False
            print("Email Address contains a space.")
            break
    if email_address[0] == "@":
        valid_address = False
        print("Email Address contains an invalid @ separator at it's start.")
    if email_address[-1] == "@":
        valid_address = False
        print("Email Address contains an invalid @ separator at it's end.")
    if valid_address:
        print("The email address is valid")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_extra_10]
    # Test valid address.
    tester.test_functions("user@host")
    # Test all mistakes.
    tester.test_functions("@user @@host@")
    # Test multiple @ signs.
    tester.test_functions("user@@host")
    # Test @ sign at start and no valid @ sign.
    tester.test_functions("@userhost")
    # Test @ sign at end and no valid @ sign.
    tester.test_functions("userhost@")
    # Test spaces.
    tester.test_functions("user @ host")


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
