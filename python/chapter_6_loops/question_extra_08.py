#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_extra_08_a():
    # -=- ANSWER START -=-
    string_ = input("Please enter a multi-word string: ")
    word_count = 1
    for letter in string_:
        if letter == " ":
            word_count += 1
    print("The number of words in the string is:", word_count)


def answer_extra_08_b():
    # -=- ANSWER START -=-
    string_ = input("Please enter a multi-word string: ")
    word_count = string_.count(" ") + 1
    print("The number of words in the string is:", word_count)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_extra_08_a, answer_extra_08_b]
    # Test many words.
    tester.test_functions(" ".join("word" + str(i) for i in range(1, 15)))
    # Test no words.
    tester.test_functions("")
    # Test single word.
    tester.test_functions("word")
    # Test blank.
    tester.test_functions("     ")


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
