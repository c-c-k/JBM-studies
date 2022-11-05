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
    a = int(input())
    b = int(input())
    print("a+b=", a + b, sep="")
    print("a-b=", a - b, sep="")
    print("a*b=", a * b, sep="")
    print("a/b=", a / b, sep="")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):
    test_input = "-81\n10\n"
    expected_output = (
        "a+b=-71\n"
        "a-b=-91\n"
        "a*b=-810\n"
        "a/b=-8.1\n"
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
