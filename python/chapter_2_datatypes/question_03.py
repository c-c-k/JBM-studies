#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper import test_answer


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    print("5+2=", 5 + 2, sep="")
    print("5-2=", 5 - 2, sep="")
    print("5*2=", 5 * 2, sep="")
    print("5/2=", 5 / 2, sep="")
    print("5//2=", 5 // 2, sep="")
    print("5%2=", 5 % 2, sep="")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):
    expected_output: str = (
        "5+2=7\n"
        "5-2=3\n"
        "5*2=10\n"
        "5/2=2.5\n"
        "5//2=2\n"
        "5%2=1\n"
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
