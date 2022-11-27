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
    low_clarity = diamond.ClarityGrade("i3")
    high_clarity = diamond.ClarityGrade("if")
    print(f"{str(low_clarity)} < {str(high_clarity)}: ", low_clarity < high_clarity)
    low_cut = diamond.CutGrade("fair")
    high_cut = diamond.CutGrade("ideal")
    print(f"{str(low_cut)} > {str(high_cut)}: ", low_cut > high_cut)


def diamond_list_load():
    with open("diamonds_test.csv", "r", newline='') as diamond_data_set:
        diamonds = csv.DictReader(diamond_data_set)
        diamond_list = DiamondList()
        for diamond_ in diamonds:
            diamond_list.add(diamond_)
        print(*diamond_list.get_iter(), sep="\n")


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


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    # test_diamond_graded_values()
    # diamond_list_load()
    # test_ui_diamonds_list_load()
    # test_ui_print_menu()
    # test_init_valid_choices()
    test_main_validate_choice()


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
