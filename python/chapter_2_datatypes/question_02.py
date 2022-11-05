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
    print("6+2=", 6 + 2, sep="")
    print("6-2=", 6 - 2, sep="")
    print("6*2=", 6 * 2, sep="")
    print("6/2=", 6 / 2, sep="")
    print("6//2=", 6 // 2, sep="")
    print("6%2=", 6 % 2, sep="")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):
    expected_output: str = (
        "6+2=8\n"
        "6-2=4\n"
        "6*2=12\n"
        "6/2=3.0\n"
        "6//2=3\n"
        "6%2=0\n"
    )

    def test_answer(self):
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
