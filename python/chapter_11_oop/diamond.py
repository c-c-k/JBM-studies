#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
# -=- ANSWER START -=-
CUT_STR_TO_INT = {
    "ideal": 5,
    "premium": 4,
    "very_good": 3,
    "good": 2,
    "fair": 1,
    "unknown": 0,
}
CLARITY_STR_TO_INT = {
    "fl": 11,
    "if": 10,
    "vvs1": 9,
    "vvs2": 8,
    "vs1": 7,
    "vs2": 6,
    "si1": 5,
    "si2": 4,
    "i1": 3,
    "i2": 2,
    "i3": 1,
    "unknown": 0,
}

BasicValue = int | float
GradedValue = int | str


class Diamond:
    cut_str_to_int: dict = {
        grade_name: grade_id for grade_name, grade_id in CUT_STR_TO_INT.items()}
    cut_int_to_str: dict = {
        grade_id: grade_name for grade_name, grade_id in CUT_STR_TO_INT.items()}
    clarity_str_to_int: dict = {
        grade_name: grade_id for grade_name, grade_id in CLARITY_STR_TO_INT.items()}
    clarity_int_to_str: dict = {
        grade_id: grade_name for grade_name, grade_id in CLARITY_STR_TO_INT.items()}
    _graded_values: dict = {
        "cut": {
            "str_to_int": cut_str_to_int,
            "int_to_str": cut_int_to_str
        },
        "clarity": {
            "str_to_int": clarity_str_to_int,
            "int_to_str": clarity_int_to_str
        }
    }
    _carat: float = None
    _cut: int = None
    _color: str = None
    _clarity: int = None
    _depth: float = None
    _table: float = None
    _price: float = None
    _x: float = None
    _y: float = None
    _z: float = None

    def __init__(
            self, carat: float = 0.0, cut: str = "",
            color: str = "", clarity: str = "", depth: float = 0.0,
            table: float = 0.0, price: float = 0.0,
            x: float = 0.0, y: float = 0.0, z: float = 0.0,
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
        
    def __str__(self):
        return (f"carat: {self.carat}, cut: {self.cut}, color: {self.color},"
                f" clarity: {self.clarity}, depth: {self.depth},"
                f" table: {self.table}, price: {self.price},"
                f" x: {self.x}, y: {self.y}, z: {self.z},")

    def _set_basic_value(self, field_name: str, value: BasicValue):
        self.__setattr__("_" + field_name, value)

    def _get_basic_value(self, field_name: str):
        return self.__getattribute__("_" + field_name)

    def _set_graded_value(self, field_name: str, grade: GradedValue, grade_map: dict):
        if isinstance(grade, str):
            try:
                grade = grade_map[grade.lower()]
            except KeyError:
                grade = 0
        elif isinstance(grade, int):
            if grade not in grade_map.values():
                grade = 0
        else:
            grade = 0
        self.__setattr__("_" + field_name, grade)

    def _get_graded_value(self, field_name: str, grade_map: dict):
        grade = self.__getattribute__("_" + field_name)
        return grade_map[grade]

    def get(self, field_name: str):
        if field_name in self._graded_values:
            return self._get_graded_value(
                field_name,
                self._graded_values[field_name]["int_to_str"]
            )
        else:
            return self._get_basic_value(field_name)

    def set(self, field_name: str, value: BasicValue | GradedValue):
        if field_name in self._graded_values:
            self._set_graded_value(
                field_name,
                value,
                self._graded_values[field_name]["str_to_int"]
            )
        else:
            self._set_basic_value(field_name, value)

    @property
    def carat(self):
        return self.get("carat")

    @carat.setter
    def carat(self, value):
        self.set("carat", value)

    @property
    def cut(self):
        return self.get("cut")

    @cut.setter
    def cut(self, value):
        self.set("cut", value)

    @property
    def color(self):
        return self.get("color")

    @color.setter
    def color(self, value):
        self.set("color", value)

    @property
    def clarity(self):
        return self.get("clarity")

    @clarity.setter
    def clarity(self, value):
        self.set("clarity", value)

    @property
    def depth(self):
        return self.get("depth")

    @depth.setter
    def depth(self, value):
        self.set("depth", value)

    @property
    def table(self):
        return self.get("table")

    @table.setter
    def table(self, value):
        self.set("table", value)

    @property
    def price(self):
        return self.get("price")

    @price.setter
    def price(self, value):
        self.set("price", value)

    @property
    def x(self):
        return self.get("x")

    @x.setter
    def x(self, value):
        self.set("x", value)

    @property
    def y(self):
        return self.get("y")

    @y.setter
    def y(self, value):
        self.set("y", value)

    @property
    def z(self):
        return self.get("z")

    @z.setter
    def z(self, value):
        self.set("z", value)


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


# -=- ANSWER END -=-
# -=- TEST START -=-


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
# class Diamond:
# __slots__ = (
#     "carat", "cut", "color", "clarity", "depth", "table", "price",
#     "x", "y", "z",
# )

# import enum
# 
# 
# class QualityEnum(enum.Enum):
#     def __eq__(self, other: "QualityEnum"):
#         if self.__class__ is other.__class__:
#             return self.value == other.value
#         else:
#             return NotImplemented
# 
#     def __ge__(self, other: "QualityEnum"):
#         if self.__class__ is other.__class__:
#             return self.value >= other.value
#         else:
#             return NotImplemented
# 
#     def __gt__(self, other: "QualityEnum"):
#         if self.__class__ is other.__class__:
#             return self.value > other.value
#         else:
#             return NotImplemented
# 
#     def __le__(self, other: "QualityEnum"):
#         if self.__class__ is other.__class__:
#             return self.value <= other.value
#         else:
#             return NotImplemented
# 
#     def __lt__(self, other: "QualityEnum"):
#         if self.__class__ is other.__class__:
#             return self.value < other.value
#         else:
#             return NotImplemented
# 
# 
# 
# 
# class Cut(enum.IntEnum):
#     FAIR = 1
#     GOOD = 2
#     VERY_GOOD = 3
#     PREMIUM = 4
#     IDEAL = 5
# 
#     @staticmethod
#     def get_cut_from_str(cut: str) -> "Cut":
#         str_to_enum = {
#             "FAIR": Cut.FAIR,
#             "GOOD": Cut.GOOD,
#             "VERY_GOOD": Cut.VERY_GOOD,
#             "PREMIUM": Cut.PREMIUM,
#             "IDEAL": Cut.IDEAL,
#         }


def main():
    print("This module is not meant to be run as main.")


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
# -=- TEST END -=-
