#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""
import enum
# ------------------------------------------------------------
# ==IMPORTS==
# ------------------------------------------------------------
# --PYTHON STANDARD LIBRARY IMPORTS--
import csv
from enum import Enum
from pathlib import Path
# --LOCAL IMPORTS--
from diamond_list import DiamondList, QueryDiamondList


# ------------------------------------------------------------
# ==PATHS==
# ------------------------------------------------------------
PATH_DIAMONDS_CSV = Path("./diamonds.csv")


# ------------------------------------------------------------
# ==ENUMS==
# ------------------------------------------------------------
class MenuChoice(Enum):
    GET_MAX_PRICE = enum.auto()
    GET_AVG_PRICE = enum.auto()
    GET_IDEAL_COUNT = enum.auto()
    GET_COLORS = enum.auto()
    GET_PREMIUM_MEDIAN_CARAT = enum.auto()
    GET_CARAT_AVG_PER_CUT = enum.auto()
    GET_PRICE_AVG_PER_COLOR = enum.auto()
    EXIT = 0


# ------------------------------------------------------------
# ==MESSAGES==
# ------------------------------------------------------------
MENU_MESSAGES: dict[MenuChoice, str] = {

    MenuChoice.GET_MAX_PRICE: (
        "Get the highest diamond price."
    ),
    MenuChoice.GET_AVG_PRICE: (
        "Get the average diamond price."
    ),
    MenuChoice.GET_IDEAL_COUNT: (
        "Count the total number of ideal diamonds in the catalog."
    ),
    MenuChoice.GET_COLORS: (
        "List the number and names of the colors available in the catalog"
    ),
    MenuChoice.GET_PREMIUM_MEDIAN_CARAT: (
        "Get the median carat for premium cut diamonds."
    ),
    MenuChoice.GET_CARAT_AVG_PER_CUT: (
        "Get the carat average per diamond cut grade."
    ),
    MenuChoice.GET_PRICE_AVG_PER_COLOR: (
        "Get the price average per diamond color."
    ),
    MenuChoice.EXIT: "Exit the diamonds program."
}


# ------------------------------------------------------------
# ==FUNCTIONS==
# ------------------------------------------------------------
def load_diamond_list() -> DiamondList | None:
    try:
        with PATH_DIAMONDS_CSV.open("r", newline='') as diamond_data_set:
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
    except (ValueError, KeyError):
        return None


def init_id_to_choice_dict() -> dict[any, MenuChoice]:
    valid_choices = {}
    for choice in MenuChoice:
        valid_choices[choice.value] = choice
    return valid_choices


def execute_choice(choice: MenuChoice, diamond_list_query: QueryDiamondList):
    if choice is MenuChoice.GET_MAX_PRICE:
        print(
            "The highest priced diamond is: ",
            diamond_list_query.get_highest_price()
        )
    elif choice is MenuChoice.GET_AVG_PRICE:
        print(
            "The average price of a diamond is: ",
            diamond_list_query.get_average_price()
        )
    elif choice is MenuChoice.GET_IDEAL_COUNT:
        print(
            "The number of Ideal diamonds is: ",
            diamond_list_query.get_count_ideal()
        )
    elif choice is MenuChoice.GET_COLORS:
        colors_info = diamond_list_query.get_colors()
        print(
            f"There are {colors_info['count']} available colors which are:"
        )
        print(
            *colors_info["color_names"], sep=", "
        )
    elif choice is MenuChoice.GET_PREMIUM_MEDIAN_CARAT:
        print(
            "The median carat for Premium diamonds is: ",
            diamond_list_query.get_premium_median_carat()
        )
    elif choice is MenuChoice.GET_CARAT_AVG_PER_CUT:
        avg_dict = diamond_list_query.get_carat_average_per_cut()
        print(
            "The carat averages per cut are: ",
            *(
                f"{cut_grade_name}: {average}"
                for cut_grade_name, average
                in avg_dict.items()
            ), sep="\n"
        )
    elif choice is MenuChoice.GET_PRICE_AVG_PER_COLOR:
        avg_dict = diamond_list_query.get_price_average_per_color()
        print(
            "The price averages per color are: ",
            *(
                f"{color}: {average}"
                for color, average
                in avg_dict.items()
            ), sep="\n"
        )


def main():
    diamond_list = load_diamond_list()
    if diamond_list is None:
        print("Exiting due to diamond list load failure ...")
        return
    diamond_list_query = QueryDiamondList(diamond_list)
    id_to_choice_dict = init_id_to_choice_dict()
    while True:
        print_menu()
        choice = input("Input number of menu choice: ")
        choice = validate_choice(choice, id_to_choice_dict)
        if choice is None:
            print("Invalid choice, please try again.")
            continue
        elif choice is MenuChoice.EXIT:
            print("Thank you for using the diamonds catalog."
                  "\nHave a nice day :)")
            return
        else:
            execute_choice(choice, diamond_list_query)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
