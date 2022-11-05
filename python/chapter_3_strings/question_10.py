#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

מקבלים בקלט רשימה של שמות שחייבים לעבור קורס נהיגה מונעת עם השם שלכם ברשימה.
הוציאו את השם שלכם מהרשימה והדפיסו אותה מחדש.
"""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.tests import test_answer


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    name_list = input()
    my_name = input()
    my_name_start_index = name_list.upper().index(my_name.upper())
    my_name_end_index = my_name_start_index + len(my_name)
    name_list = name_list[:my_name_start_index] + name_list[my_name_end_index:]
    name_list = name_list.replace("  ", " ")
    print(name_list)


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):

    def test_answer_1(self):
        self.set_stdin("fName1 lName1 fName1 lName1 fNameX mY NaMe lNameX fName1 lName1\nMY name")
        self.expected_output = "fName1 lName1 fName1 lName1 fNameX lNameX fName1 lName1\n"
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
