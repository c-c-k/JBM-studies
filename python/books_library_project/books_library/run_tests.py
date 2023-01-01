#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""

import unittest


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_loader = unittest.defaultTestLoader.discover
    test_suite = test_loader('./tests',)
    runner.run(test_suite)
