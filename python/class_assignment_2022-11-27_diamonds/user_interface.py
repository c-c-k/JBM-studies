#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# ==IMPORTS==
# ------------------------------------------------------------
from enum import Enum
from diamond_list import DiamondList
import csv


# ------------------------------------------------------------
# ==ENUMS==
# ------------------------------------------------------------
class MenuChoice(Enum):
    EXIT = 0


# ------------------------------------------------------------
# ==MESSAGES==
# ------------------------------------------------------------
MENU_MESSAGES: dict[MenuChoice, str] = {
    MenuChoice.EXIT: "Exit the diamonds program."
}


# ------------------------------------------------------------
# ==FUNCTIONS==
# ------------------------------------------------------------
def load_diamond_list() -> DiamondList | None:
    try:
        with open("diamonds_test.csv", "r", newline='') as diamond_data_set:
            diamonds = csv.DictReader(diamond_data_set)
            diamond_list = DiamondList()
            line_num = 1
            for diamond_ in diamonds:
                line_num += 1
                diamond_list.add(diamond_)
    except FileNotFoundError:
        print("Can't find diamonds dataset.")
        return None
    except ValueError as error:
        print("The diamond dataset seems to be corrupted "
              f"(line {line_num}) \n {error.args[0]}")
        return None
    else:
        return diamond_list


def print_menu():
    print("Please select action:")
    for menu_choice, menu_message in MENU_MESSAGES.items():
        print(f"  {menu_choice.value}: {menu_message}")


def validate_choice(choice, id_to_choice_dict) -> MenuChoice | None:
    try:
        return id_to_choice_dict[int(choice)]
    except (ValueError, KeyError) as error:
        print(error.__class__)
        return None


def init_id_to_choice_dict() -> dict[any, MenuChoice]:
    valid_choices = {}
    for choice in MenuChoice:
        valid_choices[choice.value] = choice
    return valid_choices


def main():
    diamond_list = load_diamond_list()
    if diamond_list is None:
        print("Exiting due to diamond list load failure ...")
        return
    id_to_choice_dict = init_id_to_choice_dict()
    while True:
        print_menu()
        choice = input("Input number of menu choice: ")
        choice = validate_choice(choice, id_to_choice_dict)
        if choice is None:
            print("Invalid choice, please try again.")
            continue
        else:
            print(choice)



# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
