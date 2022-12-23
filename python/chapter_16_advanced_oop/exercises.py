#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

import unittest
from unittest import TestCase


class Course:
    _grade: int
    _course_name: str

    def __init__(self, course_name, grade):
        self.grade = grade
        self._course_name = course_name

    @property
    def course_name(self):
        return self._course_name

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        self._grade = value

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.course_name == other.course_name
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Course):
            if self.course_name == other.course_name:
                return Course(self.course_name, (self.grade + other.grade) / 2)
            else:
                raise ValueError("can't add grades of different courses")
        else:
            return NotImplemented

    def __call__(self, failed=False, *args, **kwargs):
        if failed:
            print(f'I failed {self.course_name} class')
        else:
            print(f"I got {self.grade} in {self.course_name} class")


# homework: diner : 3 types of humburger and how to serv...


# ------------------------------------------------------------
# TESTS
# ------------------------------------------------------------
def quicktest_answers():
    pass


class TestCourse(TestCase):
    def setUp(self) -> None:
        import operator
        self.add = operator.add
        self.python1 = Course('python', 50)
        self.python2 = Course('python', 80)
        self.django = Course('django', 60)

    def test_eq(self):
        self.assertEqual(self.python1, self.python2)
        self.assertNotEqual(self.python1, self.django)
        self.assertNotEqual(self.python1, self.python1.course_name)

    def test_add(self):
        pass

    def test_call(self):
        pass


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    unittest.main(verbosity=2)
    # quicktest_answers()


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
# -=- TEST END -=-
