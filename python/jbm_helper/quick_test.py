#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
# import os
# from pathlib import Path
import sys
import typing


class QuickTest:
    __slots__ = ["functions", "mode", "suppressed_exceptions"]

    def __init__(self):
        self.functions: list[typing.Callable] | None = None
        self.mode: str | None = "input"
        self.suppressed_exceptions: list[Exception] = []

    def test(self, *args):
        if not self.functions:
            return
        if self.mode == "input":
            for function in self.functions:
                self.test_inputs_for_function(function, *args)

    def test_inputs_for_function(self, function: typing.Callable, *inputs):
        print(f"== testing function {function.__name__} with inputs: {inputs} ==")
        has_data = bool(self.mode)
        inputs = (str(input_) + "\n" for input_ in inputs)

        def stdin_readline_override() -> str:
            next_input = next(inputs)
            print(next_input, end="")
            return next_input

        if has_data:
            sys.stdin.readline_ = sys.stdin.readline
            sys.stdin.readline = stdin_readline_override
        try:
            function()
        except Exception as error:
            if type(error) in self.suppressed_exceptions:
                print(type(error), *error.args, sep=" : ")
            else:
                raise
        if has_data:
            sys.stdin.readline = sys.stdin.readline_


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    pass


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
