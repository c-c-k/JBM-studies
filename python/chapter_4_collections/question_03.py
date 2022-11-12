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
    val_dict = {val: val**3 for val in (int(input()) for _ in range(3))}
    print(val_dict)


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_1(self):
        self.set_stdin("1\n2\n3\n")
        self.expected_output = "{1: 1, 2: 8, 3: 27}\n"
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
