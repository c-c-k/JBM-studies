#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper.quick_test import QuickTest


def answer_09():
    # -=- ANSWER START -=-
    did_assignments = int(input("Did the student present all mandatory"
                                " assignments (1 for yes, 0 for no): "))
    test_score = int(input("What was the students test score? : "))
    if did_assignments:
        if test_score >= 60:
            passed_or_failed = "passed"
        else:
            passed_or_failed = "failed"
    else:
        passed_or_failed = "failed"
    print(f"The student {passed_or_failed} the the course.")


# -=- ANSWER END -=-


def answer_09_v2():
    # -=- ANSWER START -=-
    did_assignments = int(input("Did the student present all mandatory"
                                " assignments (1 for yes, 0 for no): "))
    test_score = int(input("What was the students test score? : "))
    if did_assignments and (test_score >= 60):
        passed_or_failed = "passed"
    else:
        passed_or_failed = "failed"
    print(f"The student {passed_or_failed} the the course.")


# -=- ANSWER END -=-
# -=- TEST START -=-
def quicktest_answers():
    tester = QuickTest()
    tester.functions = [answer_09, answer_09_v2]
    # Test assignments: V, score: V
    tester.test(1, 60)
    # Test assignments: V, score: X
    tester.test(1, 59)
    # Test assignments: X, score: V
    tester.test(0, 60)
    # Test assignments: X, score: X
    tester.test(0, 59)


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
