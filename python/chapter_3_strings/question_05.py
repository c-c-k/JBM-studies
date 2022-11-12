#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
import sys

from python.jbm_helper import test_answer


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    val_1 = sys.argv[1]
    val_2 = sys.argv[2]
    print(val_1, val_2, sep=":")


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_1(self):
        self.set_sysargv(["30", "10"])
        self.expected_output = "30:10\n"
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
