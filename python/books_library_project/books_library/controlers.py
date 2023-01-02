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
    Menu().execute_menu_template(MenuId.MAIN_MENU)


@register_menu_action(MenuActionID.GOTO_ERROR_MENU)
def goto_error_menu():
    Menu().execute_menu_template(MenuId.ERROR_MENU)


@register_menu_action(MenuActionID.GOTO_CUSTOMER_MENU)
def goto_customer_menu():
    Menu().execute_menu_template(MenuId.CUSTOMER_MENU)


@register_menu_action(MenuActionID.GOTO_ADD_CUSTOMER_MENU)
def goto_add_customer_menu():
    Menu().execute_menu_template(MenuId.ADD_CUSTOMER_MENU)


@register_menu_action(MenuActionID.ADD_CUSTOMER)
def add_customer(customer_info_dict):
    new_customer = CustomersModel(**customer_info_dict)
    CustomersModel.add_object(new_customer)
    Menu().select_customer(new_customer)
    Menu().execute_menu_template(MenuId.CUSTOMER_MENU)


@register_menu_action(MenuActionID.GOTO_FIND_CUSTOMER_MENU)
def goto_find_customer_menu():
    Menu().execute_menu_template(MenuId.ERROR_MENU)


@register_menu_action(MenuActionID.SELECT_CUSTOMER)
def select_customer():
    Menu().execute_menu_template(MenuId.ERROR_MENU)
    pass


@register_menu_action(MenuActionID.DELETE_CUSTOMER)
def delete_customer():
    Menu().execute_menu_template(MenuId.ERROR_MENU)
    pass


@register_menu_action(MenuActionID.GOTO_BOOKS_MENU)
def goto_books_menu():
    Menu().execute_menu_template(MenuId.BOOKS_MENU)


@register_menu_action(MenuActionID.GOTO_ADD_BOOK_MENU)
def goto_add_book_menu():
    Menu().execute_menu_template(MenuId.ADD_BOOK_MENU)


@register_menu_action(MenuActionID.ADD_BOOK)
def add_book(book_info_dict):
    new_book = BooksModel(**book_info_dict)
    BooksModel.add_object(new_book)
    Menu().add_book_to_selection(new_book)
    Menu().execute_menu_template(MenuId.BOOKS_MENU)


@register_menu_action(MenuActionID.GOTO_FIND_BOOK_MENU)
def goto_find_book_menu():
    Menu().execute_menu_template(MenuId.ERROR_MENU)


@register_menu_action(MenuActionID.SELECT_BOOK)
def select_book():
    Menu().execute_menu_template(MenuId.ERROR_MENU)
    pass


@register_menu_action(MenuActionID.DELETE_BOOK)
def delete_book():
    Menu().execute_menu_template(MenuId.ERROR_MENU)
    pass


@register_menu_action(MenuActionID.GOTO_LOANS_MENU)
def goto_loans_menu():
    Menu().execute_menu_template(MenuId.LOANS_MENU)


@register_menu_action(MenuActionID.START_LOAN)
def start_loan():
    Menu().reset_status()
    Menu().execute_menu_template(MenuId.ERROR_MENU)



@register_menu_action(MenuActionID.GOTO_ACTIVE_LOANS_MENU)
def goto_active_loans_menu():
    Menu().execute_menu_template(MenuId.ERROR_MENU)


@register_menu_action(MenuActionID.SELECT_LOAN)
def select_loan():
    Menu().execute_menu_template(MenuId.ERROR_MENU)
    pass


@register_menu_action(MenuActionID.END_LOAN)
def end_loan():
    Menu().execute_menu_template(MenuId.ERROR_MENU)
    pass


def main():
    BooksModel.load_data()
    CustomersModel.load_data()
    LoansModel.load_data()
    Menu().add_menu_templates(menu_templates)
    try:
        goto_main_menu()
    except KeyboardInterrupt:
        exit_books_library()
