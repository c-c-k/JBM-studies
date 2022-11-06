#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
import io
import sys
import typing
import unittest


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    pass


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(unittest.TestCase):
    super_stdin: typing.TextIO = None
    super_stdout: typing.TextIO = None
    test_stdin: io.StringIO = None
    test_stdout: io.StringIO = None
    test_input: str = None
    super_argv: list = None
    test_argv: list[str] = None
    expected_output: str = None

    def set_sysargv(self, test_args: list[str]):
        sys.argv = [self.super_argv[0]] + test_args

    def set_stdin(self, value: str):
        self.test_stdin = io.StringIO(value)
        sys.stdin = self.test_stdin

    def reset_std_out(self):
        self.test_stdout = io.StringIO()
        sys.stdout = self.test_stdout

    @staticmethod
    def lazy_exception_re(exception_text: str):
        return exception_text[:10] + ".*"

    def setUp(self) -> None:
        self.super_stdin = sys.stdin
        self.super_stdout = sys.stdout
        self.test_stdin = io.StringIO(initial_value=self.test_input)
        self.test_stdout = io.StringIO()
        sys.stdin = self.test_stdin
        sys.stdout = self.test_stdout
        self.super_argv = sys.argv
        sys.argv = self.test_argv

    def tearDown(self) -> None:
        sys.stdin = self.super_stdin
        sys.stdout = self.super_stdout
        self.test_stdin.close()
        self.test_stdout.close()
        sys.argv = self.super_argv

    def print_answer(self):
        self.setUp()
        main()
        output = self.test_stdout.getvalue()
        self.tearDown()
        print(output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()
