#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the "DiamondList" class's module.

"""

# ------------------------------------------------------------
# ==IMPORTS==
# ------------------------------------------------------------
# --LOCAL IMPORTS--
from diamond import Diamond


# ------------------------------------------------------------
# ==TYPES==
# ------------------------------------------------------------
BasicValue = int | float
GradedValue = int | str


# ------------------------------------------------------------
# ==CLASSES==
# ------------------------------------------------------------
class DiamondList:
    __diamond_list: list[Diamond] = None

    def __init__(self, diamond_list: list[Diamond] | None = None):
        self.__diamond_list = [] if diamond_list is None else diamond_list

    def add(self, diamond: Diamond | dict[str, str]):
        if isinstance(diamond, dict):
            try:
                diamond = Diamond(**diamond)
            except (ValueError, KeyError, TypeError) as error:
                raise ValueError("Can't load diamond from input: "
                                 f"{diamond} \n {error.args[0]}")
        self.__diamond_list.append(diamond)

    def get_all(self):
        return iter(self.__diamond_list)


# ------------------------------------------------------------
# ==FUNCTIONS==
# ------------------------------------------------------------
def main():
    print("This module is not meant to be run as main.")


# ------------------------------------------------------------
# ==PROGRAM CODE==
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
