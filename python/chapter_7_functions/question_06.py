#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


# -=- ANSWER START -=-
def auto_discount(price: int):
    if price <= 1000:
        price *= 0.9
    else:
        price *= 1 - special_discount()
    return price


def special_discount() -> float:
    discount = input("Please enter special discount in percents (like 50 or 50%): ")
    return int(discount.rstrip("%")) / 100


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [auto_discount]
    # Test price < 1000.
    tester.test_functions(
        inputs=(50,),
        args=(1000,),
        print_return=True
    )
    # Test price > 1000.
    tester.test_functions(
        inputs=(50,),
        args=(10000,),
        print_return=True
    )


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
