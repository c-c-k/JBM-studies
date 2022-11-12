#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_10_11_12():
    # -=- ANSWER START -=-
    a, b, c = map(float, input("Please enter the 'a', 'b' and 'c' parameters "
                               "of the quadratic equation separated "
                               "by spaces: ").split())
    if a == 0:
        print("Since parameter 'a' is zero these parameters do not represent "
              "a quadratic equation.")
        if b == 0:
            print("Furthermore, since parameter 'b' is also zero,"
                  " this equation isn't even a linear equation.")
            if c == 0:
                print("Rather, since even parameter 'c' is zero"
                      " this equation has an infinite number of solutions.")
            else:
                print("In fact, since parameter 'c' is not zero,"
                      "this equation doesn't have any solutions at all.")
        else:
            x = c / b
            print("The linear solution to the equation is:", x)
    else:
        from math import sqrt
        x1 = (-1 * b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        x2 = (-1 * b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        print("The roots 'x1', 'x2' of the quadratic equation are:", x1, x2)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    def quadratic_from_factorial(a, b, c, d):
        """Calculate quadratic parameters and solution from (ax-b)(cx+d)=0."""
        return (
            (
                a * c,
                a * d - b * c,
                -1 * b * d
            ),
            (
                b / a,
                -1 * (d / c)
            )
        )

    tester = QuickTest()
    tester.functions = [answer_10_11_12]

    def test_quadratic(a, b, c, d):
        """Test quadratic equation solver with parameters generated from factorial cases."""
        parameters, solutions = quadratic_from_factorial(a, b, c, d)
        tester.test_functions(" ".join(str(param) for param in parameters))
        print("The solutions should be:", *solutions)

    # Run valid quadratic tests with the help of test_quadratic.
    test_quadratic(2, 5, 1, 3)
    test_quadratic(4, 1, 3, 9)
    # Run test for linear parameters.
    tester.test_functions("0 -5 10")
    # Run test for a, b and c being zero.
    tester.test_functions("0 0 0")
    # Run test for a and b being zero and c being non-zero.
    tester.test_functions("0 0 1")


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    pass


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    quicktest_answers()
    # main()
# -=- TEST END -=-
