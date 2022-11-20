#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
# -=- ANSWER START -=-
import enum


class QualityEnum(enum.Enum):
    def __eq__(self, other: "QualityEnum"):
        if self.__class__ is other.__class__:
            return self.value == other.value
        else:
            return NotImplemented

    def __ge__(self, other: "QualityEnum"):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        else:
            return NotImplemented

    def __gt__(self, other: "QualityEnum"):
        if self.__class__ is other.__class__:
            return self.value > other.value
        else:
            return NotImplemented

    def __le__(self, other: "QualityEnum"):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        else:
            return NotImplemented

    def __lt__(self, other: "QualityEnum"):
        if self.__class__ is other.__class__:
            return self.value < other.value
        else:
            return NotImplemented




class Cut(enum.IntEnum):
    FAIR = 1
    GOOD = 2
    VERY_GOOD = 3
    PREMIUM = 4
    IDEAL = 5

    @staticmethod
    def get_cut_from_str(cut: str) -> "Cut":
        str_to_enum = {
            "FAIR": Cut.FAIR,
            "GOOD": Cut.GOOD,
            "VERY_GOOD": Cut.VERY_GOOD,
            "PREMIUM": Cut.PREMIUM,
            "IDEAL": Cut.IDEAL,
        }


class Diamond:
    __slots__ = (
        "carat", "cut", "color", "clarity", "depth", "table", "price",
        "x", "y", "z",
    )
    
    def __init__(
            self,
            carat: float, cut: str, color: str, clarity: str, depth: float,
            table: float, price: float, x: float, y: float, z: float,
    ):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.price = price
        self.x = x
        self.y = y
        self.z = z

    def get(self, field_name: str):
        return self.__getattribute__(field_name)


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

    def get_higher_than(self) -> "DiamondList":
        return self.__get_highest("price")


# -=- ANSWER END -=-
# -=- TEST START -=-


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    print("This module is not meant to be run as main.")


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
# -=- TEST END -=-
