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
    __slots__ = ["functions", "mode", "suppressed_exceptions",
                 "args", "kwargs", "inputs", "sysargv", "sysargv_orig"]

    def __init__(self):
        self.functions: list[typing.Callable] | None = None
        self.mode: str | None = "input"  # currently unused.
        self.suppressed_exceptions: list[Exception] = list()
        self.inputs: tuple = tuple()
        self.sysargv: list | None = None
        self.sysargv_orig: list = sys.argv
        self.args: tuple = tuple()
        self.kwargs: dict = dict()

    def test_functions(
            self, *_inputs_only,
            inputs: tuple | None = None,
            sysargv: list | None = None,
            args: tuple | None = None,
            kwargs: dict | None = None,
            suppressed_exceptions: tuple | None = None,
    ):
        if not self.functions:
            return
        self.inputs = inputs if inputs else _inputs_only
        self.sysargv = sysargv if sysargv else None
        self.args = args if args else tuple()
        self.kwargs = kwargs if kwargs else dict()
        self.suppressed_exceptions = suppressed_exceptions
        for function in self.functions:
            self._test_function(function)

    def _test_function(self, function: typing.Callable):
        self._print_test_info_message(function)
        self._override_sysargv()
        self._override_stdin()
        try:
            function(*self.args, **self.kwargs)
        except Exception as error:
            self._handle_suppress_exceptions(error)
        self._restore_stdin()
        self._restore_sysargv()

    def _print_test_info_message(self, function: typing.Callable):
        print(f"== testing function {function.__name__}", end="; ")
        if self.args:
            print(f"args: {self.args}", end="; ")
        if self.kwargs:
            print(f"kwargs: {self.kwargs}", end="; ")
        if self.sysargv:
            print(f"sysargv: {self.sysargv}", end="; ")
        if self.inputs:
            print(f"inputs: {self.inputs}", end="; ")
        if self.suppressed_exceptions:
            print("suppressing exceptions: "
                  f"{self.suppressed_exceptions}", end="; ")
        print("==")

    def _handle_suppress_exceptions(self, error: Exception):
        if type(error) in self.suppressed_exceptions:
            print(type(error), *error.args, sep=" : ")
        else:
            raise

    def _override_stdin(self):
        sys.stdin = StdinOverride(self.inputs)

    @staticmethod
    def _restore_stdin():
        sys.stdin = sys.__stdin__

    def _override_sysargv(self):
        if self.sysargv is not None:
            sys.argv = sys.argv[0:1]
            sys.argv.extend(self.sysargv)

    def _restore_sysargv(self):
        sys.argv = self.sysargv_orig


class StdinOverride:
    __slots__ = ["inputs"]

    def __init__(self, inputs: tuple):
        self.inputs = (str(input_) + "\n" for input_ in inputs)

    def readline(self) -> str:
        next_input = next(self.inputs)
        print(next_input, end="")
        return next_input


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main(arg1, arg2, *args, **kwargs):
    print(arg1, arg2)
    print(args, kwargs)
    print(sys.argv)
    input("input: ")
    raise ValueError


def quicktest_main():
    tester = QuickTest()
    tester.functions = [main]
    # Test helper.
    tester.test_functions(
        args=(1,),
        kwargs={"arg2": 3, "arg4": 4},
        inputs=(5, 6),
        sysargv=[7, 8],
        suppressed_exceptions=(ValueError,)
    )


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    quicktest_main()
