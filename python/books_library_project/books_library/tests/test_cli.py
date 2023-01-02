# -*- coding: utf-8 -*-

"""Summary

Description
"""

from unittest import TestCase

from interface.cli import Menu


class TestMenu(TestCase):
    def test_menu_is_singleton(self):
        menu1 = Menu()
        menu2 = Menu()
        self.assertIs(menu2, menu1)
