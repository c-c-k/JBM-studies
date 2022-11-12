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
    marks_total = int(input())
    marks_total += int(input())
    marks_total += int(input())
    marks_total += int(input())
    marks_total += int(input())
    print(round(marks_total / 5))


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_int(self):
        self.set_stdin("40\n40\n40\n40\n40\n")
        self.expected_output = "40\n"
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
