#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.tests import test_answer


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    print("X\t|X*X")
    print("-" * 16)
    num = int(input())
    print(num, num ** 2, sep="\t|")
    num = int(input())
    print(num, num ** 2, sep="\t|")
    num = int(input())
    print(num, num ** 2, sep="\t|")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_int(self):
        self.set_stdin("1\n2\n10\n")
        self.expected_output = "".join([
            "X\t|X*X\n",
            "-" * 16, "\n",
            "1\t|1\n",
            "2\t|4\n",
            "10\t|100\n",
        ])
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
