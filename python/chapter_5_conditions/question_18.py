#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.tests import test_answer


# ------------------------------------------------------------
# MESSAGES
# ------------------------------------------------------------
MSG_REQ_INPUT = "Please enter a year: "
MSG_ERROR_NON_INT_YEAR = "Year must be a whole number."
MODERN_CIV_YEAR = -4000
SINGULARITY_YEAR = 2050
MSG_ERROR_OUT_OF_CONTEXT_YEAR = ("Year must be between the start of "
                                 f"modern civilization ({abs(MODERN_CIV_YEAR)} BC) "
                                 f"and it's end ({SINGULARITY_YEAR} AC)..."
                                 )
MSG_LEAP_YEAR = "Year {YEAR} is a leap year."
MSG_NON_LEAP_YEAR = "Year {YEAR} is a normal year."


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    try:
        year = int(input(MSG_REQ_INPUT))
    except ValueError:
        raise ValueError(MSG_ERROR_NON_INT_YEAR)
    if year < MODERN_CIV_YEAR or year > SINGULARITY_YEAR:
        raise ValueError(MSG_ERROR_OUT_OF_CONTEXT_YEAR)
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        print(MSG_NON_LEAP_YEAR.format(YEAR=year))
    else:
        print(MSG_LEAP_YEAR.format(YEAR=year))


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):
    LEAP_YEARS = ("0", "2000", "-16")
    NON_LEAP_YEARS = ("1", "1000", "-1500")

    def test_non_int_input(self):
        self.set_stdin("2k\n")
        self.assertRaisesRegex(
            ValueError,
            self.lazy_exception_re(MSG_ERROR_NON_INT_YEAR),
            main,
            # msg="Accepted year with illegal characters."
        )

    def test_pre_civilization(self):
        self.set_stdin("-5000\n")
        self.assertRaisesRegex(
            ValueError,
            self.lazy_exception_re(MSG_ERROR_OUT_OF_CONTEXT_YEAR),
            main,
            # msg="Accepted pre civilization year."
        )

    def test_post_singularity(self):
        self.set_stdin("2200\n")
        self.assertRaisesRegex(
            ValueError,
            self.lazy_exception_re(MSG_ERROR_OUT_OF_CONTEXT_YEAR),
            main,
            # msg="Accepted post singularity year."
        )

    def test_leap_years(self):
        for year in self.LEAP_YEARS:
            with self.subTest("Leap year reported as non leap", year=year):
                self.set_stdin(year)
                self.reset_std_out()
                main()
                output = self.test_stdout.getvalue()
                self.expected_output = (MSG_REQ_INPUT
                                        + MSG_LEAP_YEAR.format(YEAR=year)
                                        + "\n")
                self.assertEqual(output, self.expected_output)

    def test_non_leap_years(self):
        for year in self.NON_LEAP_YEARS:
            with self.subTest("Non leap year reported as leap", year=year):
                self.set_stdin(year)
                self.reset_std_out()
                main()
                output = self.test_stdout.getvalue()
                self.expected_output = (MSG_REQ_INPUT
                                        + MSG_NON_LEAP_YEAR.format(YEAR=year)
                                        + "\n")
                self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
