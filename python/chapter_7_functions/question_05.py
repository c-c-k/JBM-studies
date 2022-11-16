#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_02():
    pass


# -=- ANSWER START -=-
def power_simple(base: float | int, exponent: int):
    """Return base to the power of exponent.

    Fractional exponents are not handled.
    :param base: The base of the power expression.
    :param exponent: The exponent of the power expression.
    :return: base taken to the power of exponent.
    """
    if int(exponent) != exponent:
        print("Can't handle fraction exponents.")
        return
    if exponent == 0:
        return 1
    result = base
    negative_exponent = exponent < 0
    exponent = abs(exponent)
    for _ in range(exponent - 1):
        result *= base
    if negative_exponent:
        result = 1 / result
    return result


def power_advanced(base: float | int, exponent: float):
    """Return base to the power of exponent.

    :param base: The base of the power expression.
    :param exponent: The exponent of the power expression.
    :return: base taken to the power of exponent.
    """

    # NOTE: "if .. return .. elif" is used to increase code clarity.
    # handle trivial case of exponent being zero.
    if exponent == 0:
        return 1
    # handle a negative non-zero exponent.
    elif exponent < 0:
        return 1 / power_advanced(base, abs(exponent))
    # handle a positive integer non-zero exponent.
    elif isinstance(exponent, int) or exponent.is_integer():
        result = base
        for _ in range(int(exponent) - 1):
            result *= base
        return result
    # handle a positive non-integer, non-zero exponent.
    else:
        return (power_advanced(base, exponent // 1)
                * _frac_power(base, exponent % 1))


def _frac_power(base: float, exponent: float) -> float:
    """Calculate a real proper fraction exponent.

    root calculation algorithm taken from:
        https://www.calculator.net/root-calculator.html
    :param base: The base of the power expression.
    :param exponent: The exponent of the power expression.
    :return: base taken to the power of exponent.
    """
    precision = 3
    root_index = round(1 / exponent)
    if (base < 0) and (root_index % 2 == 0):
        raise ValueError("Complex numbers are not supported.")
    current_root_estimate = 0
    new_root_estimate = 2
    while round(new_root_estimate - current_root_estimate, precision):
        current_root_estimate = new_root_estimate
        new_root_estimate = (
            (
                    (current_root_estimate * (root_index - 1))
                    + (base / power_advanced(current_root_estimate, root_index - 1))
            ) / root_index
            )
    return new_root_estimate


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [power_simple, power_advanced]
    # Test exponent 0.
    tester.test_functions(
        args=(2, 0,),
        print_return=True,
    )
    # Test exponent 1.
    tester.test_functions(
        args=(2, 1,),
        print_return=True,
    )
    # Test exponent -2.
    tester.test_functions(
        args=(2, -2,),
        print_return=True,
    )
    # Test exponent 1/2.
    tester.test_functions(
        args=(2, 0.5,),
        print_return=True,
        suppressed_exceptions=(ValueError,)
    )
    print("The result should be: ", pow(2, 0.5))


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
