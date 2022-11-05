#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
import sys

from python.tests import test_answer


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    dna_sequence = sys.argv[1].upper()
    print(dna_sequence[:3])
    print(dna_sequence[3:6])
    print(dna_sequence[6:9])


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_1(self):
        self.set_sysargv(["TTGCAGTCG"])
        self.expected_output = "TTG\nCAG\nTCG\n"
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)

    def test_answer_2(self):
        self.set_sysargv(["TTGCAGTCGATC"])
        self.expected_output = "TTG\nCAG\nTCG\n"
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)

    def test_answer_3(self):
        self.set_sysargv(["tcgatcgac"])
        self.expected_output = "TCG\nATC\nGAC\n"
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
