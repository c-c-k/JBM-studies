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
    net_price = float(input())
    print("raw price is:", round(net_price / 1.17))
    print("the tax is:", round(net_price - (net_price / 1.17)))


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_int(self):
        self.set_stdin("117\n")
        self.expected_output = (
            "raw price is: 100\n"
            "the tax is: 17\n"
        )
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
