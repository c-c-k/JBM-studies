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
    print("a", "b", "c=a+b", "d=a-b", "e=a*b", "f=a/b", sep="\t|")
    print("-" * 48)
    c, d, e, f = a + b, a - b, a * b, a / b
    print(a, b, c, d, e, f, sep="\t|")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):
    test_input = "-81\n10\n"
    expected_output = (
        "{}{sep}{}{sep}{}{sep}{}{sep}{}{sep}{}\n".format(
           "a", "b", "c=a+b", "d=a-b", "e=a*b", "f=a/b", sep="\t|"
        )
        + "-" * 48 + "\n"
        + "{}{sep}{}{sep}{}{sep}{}{sep}{}{sep}{}\n".format(
           "-81", "10", "-71", "-91", "-810", "-8.1", sep="\t|"
        )
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
    # main()
