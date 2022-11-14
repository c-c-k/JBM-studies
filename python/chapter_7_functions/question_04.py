#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_04():
    pass


# -=- ANSWER START -=-
def change_spliter(total_change: int):
    """Calculates and prints the bill factorisation of the input change.

    :param total_change: The change to be split into bills.
    :return: None
    """
    available_bills = (1, 5, 10, 20)
    bills_dict = init_bills_dict(available_bills)
    split_to_bills(total_change, bills_dict)
    print_bill_factors(bills_dict)


def init_bills_dict(available_bills: tuple) -> dict:
    """Initialise a bills factorisation dict from the available bills.

    :param available_bills: The available bill values from which to
                            initialise the bills_dict.
    :return: A dictionary of {bill: number of bill units} dictionary
                containing an entry for each available bill type with
                its number of bill units initialised to 0.
    """
    bills_dict = dict()
    for bill in sorted(available_bills, reverse=True):
        bills_dict[bill] = 0
    return bills_dict


def my_div_mod(dividend: int, divisor: int) -> tuple:
    whole_quotient = dividend // divisor
    return whole_quotient, dividend - whole_quotient * divisor


def split_to_bills(total_change: int, bills_dict: dict):
    """Split raw change into it's bill factors

    :param total_change: The total change to split.
    :param bills_dict: The dict containing the bill factors.
    :return: None
    """
    remaining_change = total_change
    for bill in sorted(bills_dict, reverse=True):
        bills_dict[bill], remaining_change = my_div_mod(remaining_change, bill)


def print_bill_factors(bills_dict: dict):
    """Print the bill factors in the bills_dict.

    :param bills_dict: The dictionary that contains bill factorisation.
    :return: None.
    """
    sum_check = 0
    max_msg_len = 1
    for bill, num_of_bill in bills_dict.items():
        if num_of_bill:
            bill_total = bill * num_of_bill
            sum_check += bill_total
            msg = " ".join((str(num_of_bill), "*", str(bill), "=", str(bill_total)))
            if len(msg) > max_msg_len:
                max_msg_len = len(msg)
            print(msg)
    print(max_msg_len * "-")
    print(sum_check)


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [change_spliter]
    # Test example from question.
    tester.test_functions(args=(76,))
    # Test case with no 10 bills.
    tester.test_functions(args=(66,))


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
