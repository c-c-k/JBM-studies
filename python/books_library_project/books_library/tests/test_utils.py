# -*- coding: utf-8 -*-

"""Summary

Description
"""

from unittest import TestCase

from utils import camel_to_snake_case


class TestCamelToSnakeCase(TestCase):
    def test_camel_case_with_no_initial_cap(self):
        self.assertEqual(camel_to_snake_case('camelCase'), 'camel_case')

    def test_camel_case_with_initial_cap(self):
        self.assertEqual(camel_to_snake_case('CamelCase'), 'camel_case')

    def test_camel_case_with_sequential_caps(self):
        self.assertEqual(camel_to_snake_case('CamelTMCase'), 'camel_tm_case')
        self.assertEqual(camel_to_snake_case('CamelCaseTM'), 'camel_case_tm')
