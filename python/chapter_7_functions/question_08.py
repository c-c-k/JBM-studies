#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


# -=- ANSWER START -=-
def menu(a: float, b: float):
    menu_display = "\n".join((
        "a - the biggest divider"
        "b- the smallest divider"
        "c- the result of pow(a, b)"
        "d - the; result; of; sqrt(a) - sqrt(b)]"
        "e - exit"
    ))

        print(menu_display)
        choice = input("Please enter desired operation: ")
        if choice == "e":
            break
        elif choice == "a":
            pass
        elif choice == "b":
            pass
        elif choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("wrong choice, ", end="")




# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [menu]
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
