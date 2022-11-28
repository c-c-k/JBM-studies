#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest
import diamond
from diamond_list import DiamondList
import user_interface as ui
import csv


def test_diamond_graded_values():
    print("--clarity and cut grade tests::")
    low_clarity = diamond.ClarityGrade("I3")
    high_clarity = diamond.ClarityGrade("IF")
    print(
        f"{str(low_clarity)} < {str(high_clarity)}: ",
        low_clarity < high_clarity
    )
    low_cut = diamond.CutGrade("Fair")
    high_cut = diamond.CutGrade("Ideal")
    print(
        f"{str(low_cut)} > {str(high_cut)}: ",
        low_cut > high_cut
    )


def diamond_list_load():
    with open("diamonds_test.csv", "r", newline='') as diamond_data_set:
        diamonds = csv.DictReader(diamond_data_set)
        diamond_list = DiamondList()
        for diamond_ in diamonds:
            diamond_list.add(diamond_)
        print(*iter(diamond_list), sep="\n")


def test_ui_diamonds_list_load():
    tester = QuickTest()
    tester.functions = [ui.load_diamond_list]
    tester.test_functions(print_return=True)


def test_ui_print_menu():
    tester = QuickTest()
    tester.functions = [ui.print_menu]
    tester.test_functions(print_return=True)


def test_init_valid_choices():
    tester = QuickTest()
    tester.functions = [ui.init_id_to_choice_dict]
    tester.test_functions(print_return=True)


def test_main_validate_choice():
    tester = QuickTest()
    tester.functions = [ui.main]
    tester.test_functions(
        print_return=True,
        inputs=("string", 0.0, 99999, 0)
    )


def test_main_choice(choice: ui.MenuChoice):
    tester = QuickTest()
    tester.functions = [ui.main]
    tester.test_functions(
        print_return=True,
        inputs=(choice.value, 0)
    )


def test_main_choice_max_price():
    test_main_choice(ui.MenuChoice.GET_MAX_PRICE)


def test_main_choice_avg_price():
    test_main_choice(ui.MenuChoice.GET_AVG_PRICE)


def test_main_choice_ideal_count():
    test_main_choice(ui.MenuChoice.GET_IDEAL_COUNT)


def test_main_choice_colors():
    test_main_choice(ui.MenuChoice.GET_COLORS)


def test_main_choice_premium_median_carat():
    test_main_choice(ui.MenuChoice.GET_PREMIUM_MEDIAN_CARAT)


def test_main_choice_carat_avg_per_cut():
    test_main_choice(ui.MenuChoice.GET_CARAT_AVG_PER_CUT)


def test_main_choice_price_avg_per_color():
    test_main_choice(ui.MenuChoice.GET_PRICE_AVG_PER_COLOR)


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    test_diamond_graded_values()
    diamond_list_load()
    test_ui_diamonds_list_load()
    test_ui_print_menu()
    test_init_valid_choices()
    test_main_validate_choice()
    test_main_choice_max_price()
    test_main_choice_avg_price()
    test_main_choice_ideal_count()
    test_main_choice_colors()
    test_main_choice_premium_median_carat()
    test_main_choice_carat_avg_per_cut()
    test_main_choice_price_avg_per_color()


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
