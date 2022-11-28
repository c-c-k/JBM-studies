#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the "DiamondList" class's module.

"""

# ------------------------------------------------------------
# ==IMPORTS==
# ------------------------------------------------------------
# --PYTHON STANDARD LIBRARY IMPORTS--
import statistics
# --LOCAL IMPORTS--
from diamond import Diamond, CutGrade


# ------------------------------------------------------------
# ==TYPES==
# ------------------------------------------------------------


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

    def __len__(self):
        return len(self.__diamond_list)

    def __getitem__(self, item):
        return self.__diamond_list[item]

    def __iter__(self):
        return iter(self.__diamond_list)

    def __contains__(self, item):
        return item in self.__diamond_list

    def __copy__(self):
        return self.__diamond_list[:]


class QueryDiamondList:
    __diamond_list: DiamondList = None

    def __init__(self, diamond_list: DiamondList):
        self.__diamond_list = diamond_list

    def get_highest_price(self) -> int:
        return max((
            diamond.price
            for diamond
            in iter(self.__diamond_list)
        ))

    def get_average_price(self) -> int:
        return round(statistics.mean((
            diamond.price
            for diamond
            in iter(self.__diamond_list)
        )))

    def get_count_ideal(self) -> int:
        cut_grade = CutGrade("Ideal")
        return sum((
            1 for diamond
            in iter(self.__diamond_list)
            if diamond.cut == cut_grade
        ))

    def get_color_names(self) -> set[str]:
        return set((
            diamond.color
            for diamond
            in iter(self.__diamond_list)
        ))

    def get_colors(self) -> dict[str, int | set[str]]:
        color_names = self.get_color_names()
        return {
            "count": len(color_names),
            "color_names": color_names
        }

    def get_premium_median_carat(self) -> float:
        cut_grade = CutGrade("Premium")
        return statistics.median((
            diamond.carat
            for diamond
            in iter(self.__diamond_list)
            if diamond.cut == cut_grade
        ))

    def get_carat_average_per_cut(self) -> dict[str, float]:
        cut_grades = {
            CutGrade(grade_name): 0
            for grade_name
            in CutGrade.name_to_id.keys()
        }
        for cut_grade in cut_grades.keys():
            cut_grades[cut_grade] = statistics.mean((
                diamond.carat
                for diamond
                in iter(self.__diamond_list)
                if diamond.cut == cut_grade
            ))
        return {
            str(cut_grade): round(average, 2)
            for cut_grade, average
            in cut_grades.items()
        }

    def get_price_average_per_color(self) -> dict[str, int]:
        colors = {
            color: 0
            for color
            in self.get_color_names()
        }
        for color in colors.keys():
            colors[color] = statistics.mean((
                diamond.price
                for diamond
                in iter(self.__diamond_list)
                if diamond.color == color
            ))
        return {
            color: round(average)
            for color, average
            in colors.items()
        }


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
