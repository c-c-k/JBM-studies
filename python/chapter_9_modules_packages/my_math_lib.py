#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
# -=- ANSWER START -=-
from math import sqrt

Number = int | float
NumberN = Number | None

lib_initiated = False


def init_lib():
    global lib_initiated
    lib_initiated = True


def _is_not_initiated() -> bool:
    if not lib_initiated:
        print("init_lib must be run before calling any of the module functions.")
        return True
    else:
        return False


# noinspection PyShadowingBuiltins
def max(val1: Number, val2: Number) -> NumberN:
    if _is_not_initiated():
        return
    if val1 > val2:
        return val1
    else:
        return val2


# noinspection PyShadowingBuiltins
def min(val1: Number, val2: Number) -> NumberN:
    if _is_not_initiated():
        return
    if val1 < val2:
        return val1
    else:
        return val2


def mean(values: list[Number]) -> NumberN:
    if _is_not_initiated():
        return
    # Mean formula:
    #   sum(values) / number of values
    sum_ = 0
    for value in values:
        sum_ += value
    return sum_ / len(values)


def std(values: list[Number]) -> NumberN:
    if _is_not_initiated():
        return
    # Standard deviation formula:
    #   sqrt(sum((value - mean)**2) / number of values)
    sum_ = 0
    mean_ = mean(values)
    for value in values:
        sum_ += (value - mean_) ** 2
    return sqrt(sum_ / len(values))


# -=- ANSWER END -=-
# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    print("This module is only meant for import, not direct execution!")


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
