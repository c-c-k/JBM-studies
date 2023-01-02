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


@register_menu_action(MenuActionID.GOTO_MAIN_MENU)
def goto_main_menu():
    pass


@register_menu_action(MenuActionID.GOTO_ERROR_MENU)
def goto_error_menu():
    pass


@register_menu_action(MenuActionID.GOTO_CUSTOMER_MENU)
def goto_customer_menu():
    pass


@register_menu_action(MenuActionID.GOTO_ADD_CUSTOMER_MENU)
def goto_add_customer_menu():
    pass


@register_menu_action(MenuActionID.ADD_CUSTOMER)
def add_customer():
    pass


@register_menu_action(MenuActionID.GOTO_FIND_CUSTOMER_MENU)
def goto_find_customer_menu():
    pass


@register_menu_action(MenuActionID.# LOOKUP_CUSTOMERS)
def # lookup_customers():
    pass


@register_menu_action(MenuActionID.SELECT_CUSTOMER)
def select_customer():
    pass


@register_menu_action(MenuActionID.DELETE_CUSTOMER)
def delete_customer():
    pass


@register_menu_action(MenuActionID.GOTO_BOOKS_MENU)
def goto_books_menu():
    pass


@register_menu_action(MenuActionID.GOTO_ADD_BOOK_MENU)
def goto_add_book_menu():
    pass


@register_menu_action(MenuActionID.ADD_BOOK)
def ADD_BOOK():
    pass


@register_menu_action(MenuActionID.GOTO_FIND_BOOK_MENU)
def goto_find_book_menu():
    pass


@register_menu_action(MenuActionID.# LOOKUP_BOOKS)
def # lookup_books():
    pass


@register_menu_action(MenuActionID.SELECT_BOOK)
def select_book():
    pass


@register_menu_action(MenuActionID.DELETE_BOOK)
def delete_book():
    pass


@register_menu_action(MenuActionID.GOTO_LOANS_MENU)
def goto_loans_menu():
    pass


@register_menu_action(MenuActionID.START_LOAN)
def start_loan():
    pass


@register_menu_action(MenuActionID.GOTO_ACTIVE_LOANS_MENU)
def goto_active_loans_menu():
    pass


@register_menu_action(MenuActionID.SELECT_LOAN)
def select_loan():
    pass


@register_menu_action(MenuActionID.END_LOAN)
def end_loan():
    pass




def main():
    BooksModel.load_data()
    CustomersModel.load_data()
    LoansModel.load_data()
    Menu().add_menu_templates(menu_templates)
    try:
        Menu().execute_menu_template(MenuId.MAIN_MENU)
    except KeyboardInterrupt:
        exit_books_library()
