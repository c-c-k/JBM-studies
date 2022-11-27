#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains the 'Diamond' class and it's supplements.

Classes:
    * Diamond - This class represents a single diamond.
    * BaseGrade - A base class for graded values (string values that
                    represent sortable grades.)
    * CutGrade - A BaseGrade derivative for diamond cut grades.
    * ClarityGrade - A BaseGrade derivative for diamond clarity grades.
Types:
    * TypeGradedValue: A convenience type for the possible input values
                        for the BaseGrade initializer.
"""


# ------------------------------------------------------------
# ==IMPORTS==
# ------------------------------------------------------------


# ------------------------------------------------------------
# ==TYPES==
# ------------------------------------------------------------
#  A convenience type for the possible input values
#  for the BaseGrade initializer.
TypeGradedValue = int | str


# ------------------------------------------------------------
# ==CUSTOM EXCEPTIONS==
# ------------------------------------------------------------


# ------------------------------------------------------------
# ==CLASSES==
# ------------------------------------------------------------
class BaseGrade:
    """A base class for graded values.
    The purpose of this class is to allow sorting for string diamond
    attributes that represent diamond qualities that have
    a clear grade ladder.

    attributes:
        * name_to_id: A dictionary mapping the string names of the grades
                        as they appear in the source dataset to integer id's
                        that would allow convenient sorting.
                        This attribute needs to be overriden
                        with the appropriate mapping in each inheriting class.
                        NOTE: Make sure the id's mapped to the grade names
                            match the intended grade ladder.
        * id_to_name: An inverse mapping of name_to_id meant for returning
                        the grade names mapped to the grade id's for purposes
                        of output.
                        NOTE: each inheritor class should override this
                        attribute with:
                            id_to_name = {
                                grade_id: grade_name for grade_name,
                                 grade_id in name_to_id.items()}
                        TODO: Think of a way to do this automatically for
                                each inheritor without adding a lot of
                                overhead.
        * _grade_id: The integer grade id that has been set for a particular
            instance of an inheritor class.
    Properties:
        * grade: Returns the integer grade id of an instance and sets it
                according to input type.
    """
    name_to_id: dict[str, int] = {}
    id_to_name: dict[int, str] = {}
    _grade_id: int = None

    def __init__(self, grade: TypeGradedValue):
        """

        :param grade: The string or integer value according to which
                        the grade id of the instance is to be set.
        """
        self.grade = grade

    @property
    def grade(self):
        """

        return: The integer grade id of the instance.
        """
        return self._grade_id

    @grade.setter
    def grade(self, grade: TypeGradedValue):
        """Set the integer grade id of the instance.

        If the input grade is a str try to convert it to a grade id via
            the mapping given in self.name_to_id.
        If the input grade is an int try to set it as the grade id if
            it represents a valid grade id.
        :raise ValueError if the grade value is illegal.
        :param grade: The raw (int id or str name) grade from which the
                        instances grade id is to be set.
        """
        if isinstance(grade, int) and (grade in self.id_to_name.keys()):
            self._grade_id = grade
        elif isinstance(grade, str) and (grade in self.name_to_id.keys()):
            self._grade_id = self.name_to_id[grade]
        else:
            raise ValueError(f"Wrong graded value: '{grade}' for: '"
                             f"{self.__class__.__name__}")

    def __copy__(self):
        return self.__class__(self._grade_id)

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


class CutGrade(BaseGrade):
    """A BaseGrade inheritor for diamond cut grades.

    The cut grades follow what seemed to me to be the obvious grade ladder:
        ideal > premium > very_good > good > fair
    """
    name_to_id = {
        "Ideal": 5,
        "Premium": 4,
        "Very Good": 3,
        "Good": 2,
        "Fair": 1,
    }
    id_to_name = {
        grade_id: grade_name for grade_name, grade_id in name_to_id.items()}


class ClarityGrade(BaseGrade):
    """A BaseGrade inheritor for diamond clarity grades.


    The clarity ratings follow the official ratings taken from
    'https://www.tiffany.com/engagement/
        the-tiffany-guide-to-diamonds/clarity/':
        fl > if > vvs1 > vvs2 > vs1 > vs2 > si1 > si2 > i1 > i2 > i3

    """
    name_to_id = {
        "FL": 11,
        "IF": 10,
        "VVS1": 9,
        "VVS2": 8,
        "VS1": 7,
        "VS2": 6,
        "SI1": 5,
        "SI2": 4,
        "I1": 3,
        "I2": 2,
        "I3": 1,
    }
    id_to_name = {
        grade_id: grade_name for grade_name, grade_id in name_to_id.items()}


class Diamond:
    """ This class represents a single diamond.

    All the diamond's slot attributes correspond to the field names(and
    meanings) in the diamonds' dataset.
    """
    __slots__ = [
        "carat", "cut", "color", "clarity",
        "depth", "table", "price", "x", "y", "z"
    ]

    def __init__(
            self, carat: float = 0.0, cut: TypeGradedValue = "",
            color: str = "", clarity: TypeGradedValue = "", depth: float = 0.0,
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
        self.carat = float(carat)
        self.cut = CutGrade(cut)
        self.color = color
        self.clarity = ClarityGrade(clarity)
        self.depth = float(depth)
        self.table = float(table)
        self.price = int(price)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return (f"carat: {self.carat}, cut: {self.cut}, color: {self.color},"
                f" clarity: {self.clarity}, depth: {self.depth},"
                f" table: {self.table}, price: {self.price},"
                f" x: {self.x}, y: {self.y}, z: {self.z},")

    def __copy__(self):
        return self.__class__(*self.__slots__)


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
