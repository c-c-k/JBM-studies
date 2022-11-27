#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the "Diamond" class's module.

"""


# ------------------------------------------------------------
# ==IMPORTS==
# ------------------------------------------------------------


# ------------------------------------------------------------
# ==TYPES==
# ------------------------------------------------------------
BasicValue = int | float
TypeGraded = int | str


# ------------------------------------------------------------
# ==CUSTOM EXCEPTIONS==
# ------------------------------------------------------------


# ------------------------------------------------------------
# ==CLASSES==
# ------------------------------------------------------------
class GradedValue:
    name_to_id: dict[str, int] = {}
    id_to_name: dict[int, str] = {}
    _grade_id: int = None

    def __init__(self, grade: TypeGraded):
        # self._name_to_id = self.cl
        self.grade = grade

    @property
    def grade(self):
        return self._grade_id

    @grade.setter
    def grade(self, grade: TypeGraded):
        if isinstance(grade, int) and (grade in self.id_to_name.keys()):
            self._grade_id = grade
        elif isinstance(grade, str) and (grade in self.name_to_id.keys()):
            self._grade_id = self.name_to_id[grade]
        else:
            raise ValueError(f"Wrong graded value for class: {self.__class__}")

    def __repr__(self):
        return f"class: {self.__class__}, _grade_id: {self._grade_id}"

    def __str__(self):
        if self._grade_id is not None:
            return self.id_to_name[self._grade_id]
        else:
            return "Undefined"

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.grade == other.grade

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.grade >= other.grade

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.grade > other.grade

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.grade <= other.grade

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.grade < other.grade


class GradedValueCut(GradedValue):
    """

    For purposes on comparison, the cut and clarity ratings
    follow the official ratings:
        ideal > premium > very_good > good > fair
    """
    name_to_id = {
        "ideal": 5,
        "premium": 4,
        "very_good": 3,
        "good": 2,
        "fair": 1,
    }
    id_to_name = {
        grade_id: grade_name for grade_name, grade_id in name_to_id.items()}


class GradedValueClarity(GradedValue):
    """

    For purposes on comparison, the clarity ratings
    follow the official ratings:
        fl > if > vvs1 > vvs2 > vs1 > vs2 > si1 > si2 > i1 > i2 > i3
    """
    name_to_id = {
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
    }
    id_to_name = {
        grade_id: grade_name for grade_name, grade_id in name_to_id.items()}


class Diamond:
    """
    This class represents a single diamond.

    """
    def __init__(
            self, carat: float = 0.0, cut: TypeGraded = "",
            color: str = "", clarity: TypeGraded = "", depth: float = 0.0,
            table: float = 0.0, price: float = 0.0,
            x: float = 0.0, y: float = 0.0, z: float = 0.0,
    ):
        """

        :param carat: The diamonds carat value.
        :param cut: The diamonds cut rating.
        :param color: The diamonds color classification.
        :param clarity: The diamonds clarity rating.
        :param depth: The diamonds depth.
        :param table: The diamonds table rating.
        :param price: The diamonds market price.
        :param x: The diamonds length.
        :param y: The diamonds width.
        :param z: The diamonds height.
        """
        self.carat = carat
        self.cut = GradedValueCut(cut)
        self.color = color
        self.clarity = GradedValueClarity(clarity)
        self.depth = depth
        self.table = table
        self.price = price
        self.x = x
        self.y = y
        self.z = z

    # -- Magic methods overrides --
    def __str__(self):
        return (f"carat: {self.carat}, cut: {self.cut}, color: {self.color},"
                f" clarity: {self.clarity}, depth: {self.depth},"
                f" table: {self.table}, price: {self.price},"
                f" x: {self.x}, y: {self.y}, z: {self.z},")


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
# -=- TEST END -=-
