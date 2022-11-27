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

    def add(self, diamond: Diamond):
        self.__diamond_list.append(diamond)

    def remove_carat(self, carat: float):
        new_diamond_list = list()
        while self.__diamond_list:
            diamond = self.__diamond_list.pop()
            if diamond.carat != carat:
                new_diamond_list.append(diamond)

    def get_all(self):
        return iter(self.__diamond_list)

    def __get_highest(self, field_name) -> "DiamondList":
        diamond_iter = self.get_all()
        diamond = next(diamond_iter)
        highest_list = [diamond]
        max_val = diamond.get(field_name)
        for diamond in diamond_iter:
            val = diamond.get(field_name)
            if val == max_val:
                highest_list.append(diamond)
            elif val > max_val:
                max_val = val
                highest_list = [diamond]
        return DiamondList(highest_list)

    def get_highest_carat(self) -> "DiamondList":
        return self.__get_highest("carat")


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
