#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""

import unittest

from tests.test_dal import suite_fields


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite_fields())

