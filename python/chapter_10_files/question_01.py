#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest
# -=- ANSWER START -=-
import enum
from pathlib import Path
import random


class Operator(enum.Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


Question = tuple[int, Operator, int]

questions_file = Path("/dev/shm/math_test_questions.txt")
answers_file = Path("/dev/shm/math_test_answers.txt")


def answer_01():
    with questions_file.open("w") as qf:
        with answers_file.open("w") as af:
            for _ in range(10):
                question = gen_question()
                qf.write(gen_question_text(question) + "\n")
                af.write(gen_answer_text(question) + "\n")


def gen_question() -> Question:
    return (
        random.randrange(11),
        random.choice([operator for operator in Operator]).value,
        random.randrange(11),
    )


def gen_question_text(question: Question) -> str:
    return "{}{}{}".format(*question)


def gen_answer_text(question: Question) -> str:
    return f"{gen_question_text(question)}={calc_answer(question)}"


def calc_answer(question: Question) -> int | float | str:
    operand_1, operator, operand_2 = question
    if operator is Operator.ADD:
        return operand_1 + operand_2
    elif operator is Operator.SUBTRACT:
        return operand_1 - operand_2
    elif operator is Operator.MULTIPLY:
        return operand_1 * operand_2
    else:
        try:
            return round(operand_1 / operand_2, 2)
        except ZeroDivisionError:
            return "!ZERO DIVISION!"


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_01]
    answer_01()
    print("-- questions --")
    print(questions_file.read_text())
    print("-- answers --")
    print(answers_file.read_text())


# ------------------------------------------------------------
# --UNUSED
# ------------------------------------------------------------
def main():
    pass


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    quicktest_answers()
    # main()
# -=- TEST END -=-
