#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""

import unittest

# import tests

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    # test_loader = unittest.defaultTestLoader.loadTestsFromModule
    # test_suite = unittest.TestSuite((
    #     test_loader(test_fields),
    # ))
    # test_loader = unittest.defaultTestLoader.loadTestsFromNames
    # test_suite = test_loader((
    #     tests.test_fields,
    #     tests.test_utils,
    # ), tests)
    test_loader = unittest.defaultTestLoader.discover
    test_suite = test_loader('./tests',)
    runner.run(test_suite)
