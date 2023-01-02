# -*- coding: utf-8 -*-

"""Summary

Description
"""

from enum import Enum, auto
import re

from interface.template import MenuTemplate, MenuChoice


class MenuId(Enum):
    MAIN_MENU = auto()
    ERROR_MENU = auto()
    CUSTOMER_MENU = auto()
    ADD_CUSTOMER_MENU = auto()
    FIND_CUSTOMER_MENU = auto()
    BOOKS_MENU = auto()
    ADD_BOOK_MENU = auto()
    FIND_BOOK_MENU = auto()
    LOANS_MENU = auto()
    ACTIVE_LOANS_MENU = auto()


class MenuActionID(Enum):
    EXIT = auto()
    GOTO_MAIN_MENU = auto()
    GOTO_ERROR_MENU = auto()
    GOTO_CUSTOMER_MENU = auto()
    GOTO_ADD_CUSTOMER_MENU = auto()
    ADD_CUSTOMER = auto()
    GOTO_FIND_CUSTOMER_MENU = auto()
    LOOKUP_CUSTOMERS = auto()
    SELECT_CUSTOMER = auto()
    DELETE_CUSTOMER = auto()
    GOTO_BOOKS_MENU = auto()
    GOTO_ADD_BOOK_MENU = auto()
    ADD_BOOK = auto()
    GOTO_FIND_BOOK_MENU = auto()
    LOOKUP_BOOKS = auto()
    SELECT_BOOK = auto()
    DELETE_BOOK = auto()
    GOTO_LOANS_MENU = auto()
    START_LOAN = auto()
    GOTO_ACTIVE_LOANS_MENU = auto()
    SELECT_LOAN = auto()
    END_LOAN = auto()


menu_templates = {
    MenuId.MAIN_MENU: MenuTemplate(
        menu_id=MenuId.MAIN_MENU,
        menu_path='main menu',
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.GOTO_CUSTOMER_MENU,
                choice_token='c',
                choice_text='Enter customers menu.'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_BOOKS_MENU,
                choice_token='b',
                choice_text='Enter books menu.'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_LOANS_MENU,
                choice_token='l',
                choice_text='Enter loans menu.'
            ),
            MenuChoice(
                choice_id=MenuActionID.EXIT,
                choice_token='e',
                choice_text='Exit the books library.'
            ),
        )
    ),
    MenuId.CUSTOMER_MENU: MenuTemplate(
        menu_id=MenuId.CUSTOMER_MENU,
        menu_path='main menu -> customers menu',
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.GOTO_ADD_CUSTOMER_MENU,
                choice_token='r',
                choice_text='Register a new customer'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_FIND_CUSTOMER_MENU,
                choice_token='f',
                choice_text='Find an existing customer'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_MAIN_MENU,
                choice_token='m',
                choice_text='Return to main menu'
            ),
        )
    ),
    MenuId.ADD_CUSTOMER_MENU: MenuTemplate(
        menu_id=MenuId.ADD_CUSTOMER_MENU,
        menu_path='main menu -> customers menu -> add customer',
        is_custom_input_menu=True,
        custom_input_handler_id=MenuActionID.ADD_CUSTOMER,
        custom_input_header=(
            'Please enter the name, age and city '
            'of residence of the new customer.\n'
            'The input format should be: <NAME>;<AGE>;<CITY>'
        ),
        custom_input_pattern=re.compile(
            r'(?P<name>[^;]+);(?P<age>\d+);(?P<city>[^;]+);?'),
    ),
    MenuId.FIND_CUSTOMER_MENU: MenuTemplate(
        menu_id=MenuId.FIND_CUSTOMER_MENU,
        menu_path='main menu -> customers menu -> find customer',
        is_selection_menu=True,
        selection_handler_id=MenuActionID.SELECT_CUSTOMER,
    ),
}
