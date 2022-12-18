#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


def multiply_by_constant_factory(constant):
    def multiply_by_constant(number):
        return constant * number
    return multiply_by_constant


def myzip(*iterables):
    iterators = tuple(iter(iterable) for iterable in iterables)
    while True:
        try:
            yield tuple(next(iterator) for iterator in iterators)
        except RuntimeError:
            return


def gen_filter_factory(num):
    def filter_by_num(raw_list):
        return [val for val in raw_list if not val % num]
    return filter_by_num


def gr_then_factory(num):
    return lambda val: val > num


# ------------------------------------------------------------
# TESTS
# ------------------------------------------------------------
def quicktest_answers():
    multiply_by_2 = multiply_by_constant_factory(2)
    print(multiply_by_2(3))
    filter_by_3 = gen_filter_factory(3)
    print(filter_by_3(list(range(30))))
    gr_then_30 = gr_then_factory(30)
    print(gr_then_30(30), gr_then_30(31))
    print(*myzip(range(3), range(5), range(3)))


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
