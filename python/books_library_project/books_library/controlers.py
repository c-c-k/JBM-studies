# -*- coding: utf-8 -*-

"""Summary

Description
"""

from enum import Enum

from interface.cli import Menu
from models import BooksModel, CustomersModel, LoansModel
from views import MenuActionID, menu_templates, MenuId


def register_menu_action(menu_action_id: Enum):
    def registrator(func):
        Menu().register_menu_action(menu_action_id, func)
        return func
    return registrator


@register_menu_action(MenuActionID.EXIT)
def exit_books_library():
    BooksModel.save_data()
    CustomersModel.save_data()
    LoansModel.save_data()
    Menu().exit()


def main():
    BooksModel.load_data()
    CustomersModel.load_data()
    LoansModel.load_data()
    Menu().add_menu_templates(menu_templates)
    try:
        Menu().execute_menu_template(MenuId.MAIN_MENU)
    except KeyboardInterrupt:
        exit_books_library()
