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
    CUSTOMER_ACTIONS_MENU = auto()
    BOOKS_MENU = auto()
    ADD_BOOK_MENU = auto()
    FIND_BOOK_MENU = auto()
    BOOK_ACTIONS_MENU = auto()
    LOANS_MENU = auto()
    ACTIVE_LOANS_MENU = auto()
    LOAN_ACTIONS_MENU = auto()


class MenuActionID(Enum):
    EXIT = auto()
    GOTO_MAIN_MENU = auto()
    GOTO_ERROR_MENU = auto()
    GOTO_CUSTOMER_MENU = auto()
    GOTO_ADD_CUSTOMER_MENU = auto()
    ADD_CUSTOMER = auto()
    GOTO_FIND_CUSTOMER_MENU = auto()
    # LOOKUP_CUSTOMERS = auto()
    SELECT_CUSTOMER = auto()
    DELETE_CUSTOMER = auto()
    GOTO_BOOKS_MENU = auto()
    GOTO_ADD_BOOK_MENU = auto()
    ADD_BOOK = auto()
    GOTO_FIND_BOOK_MENU = auto()
    # LOOKUP_BOOKS = auto()
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
    MenuId.ERROR_MENU: MenuTemplate(
        menu_id=MenuId.ERROR_MENU,
        menu_path='-- ERROR --',
        menu_header=(
            'We are sorry, something went wrong :('
        ),
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.GOTO_MAIN_MENU,
                choice_token='m',
                choice_text='Return to main menu'
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
    MenuId.CUSTOMER_ACTIONS_MENU: MenuTemplate(
        menu_id=MenuId.CUSTOMER_ACTIONS_MENU,
        menu_path=('main menu -> customers menu '
                   '-> find customer -> customer actions'),
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.SELECT_CUSTOMER,
                choice_token='s',
                choice_text='Select this customer as book loaner'
            ),
            MenuChoice(
                choice_id=MenuActionID.DELETE_CUSTOMER,
                choice_token='d',
                choice_text='Delete this customer from database'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_CUSTOMER_MENU,
                choice_token='c',
                choice_text='Return to customers menu'
            ),
        )
    ),
    MenuId.BOOKS_MENU: MenuTemplate(
        menu_id=MenuId.BOOKS_MENU,
        menu_path='main menu -> books menu',
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.GOTO_ADD_BOOK_MENU,
                choice_token='a',
                choice_text='add a new book'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_FIND_BOOK_MENU,
                choice_token='f',
                choice_text='Find an existing book'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_MAIN_MENU,
                choice_token='m',
                choice_text='Return to main menu'
            ),
        )
    ),
    MenuId.ADD_BOOK_MENU: MenuTemplate(
        menu_id=MenuId.ADD_BOOK_MENU,
        menu_path='main menu -> books menu -> add book',
        is_custom_input_menu=True,
        custom_input_handler_id=MenuActionID.ADD_BOOK,
        custom_input_header=(
            'Please enter the name, author, year of publication '
            'and loan type of the new book.\n'
            'Available loan types are: 1- 10 days, 2- 5 days, 3- 2 days.\n'
            'The input format should be: '
            '<NAME>;<AUTHOR>;<YEAR OF PUBLICATION>;<LOAN TYPE>'
        ),
        custom_input_pattern=re.compile(
            r'(?P<name>[^;]+);(?P<author>[^;]+);'
            r'(?P<year_published>\d{1,4});(?P<loan_type>\d);?'),
    ),
    MenuId.FIND_BOOK_MENU: MenuTemplate(
        menu_id=MenuId.FIND_BOOK_MENU,
        menu_path='main menu -> books menu -> find book',
        is_selection_menu=True,
        selection_handler_id=MenuActionID.SELECT_BOOK,
    ),
    MenuId.BOOK_ACTIONS_MENU: MenuTemplate(
        menu_id=MenuId.BOOK_ACTIONS_MENU,
        menu_path=('main menu -> books menu '
                   '-> find book -> book actions'),
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.SELECT_BOOK,
                choice_token='a',
                choice_text='Add this book to loan list'
            ),
            MenuChoice(
                choice_id=MenuActionID.DELETE_BOOK,
                choice_token='d',
                choice_text='Delete this book from database'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_BOOKS_MENU,
                choice_token='c',
                choice_text='Return to books menu'
            ),
        )
    ),
    MenuId.LOANS_MENU: MenuTemplate(
        menu_id=MenuId.LOANS_MENU,
        menu_path='main menu -> loans menu ',
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.START_LOAN,
                choice_token='l',
                choice_text='Loan the selected books to the selected customer'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_ACTIVE_LOANS_MENU,
                choice_token='s',
                choice_text='Show all currently active loans'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_BOOKS_MENU,
                choice_token='m',
                choice_text='Return to main menu'
            ),
        )
    ),
    MenuId.ACTIVE_LOANS_MENU: MenuTemplate(
        menu_id=MenuId.ACTIVE_LOANS_MENU,
        menu_path='main menu -> loans menu -> active loans',
        is_selection_menu=True,
        selection_handler_id=MenuActionID.SELECT_LOAN,
    ),
    MenuId.LOAN_ACTIONS_MENU: MenuTemplate(
        menu_id=MenuId.LOAN_ACTIONS_MENU,
        menu_path='main menu -> loans menu -> active loans -> loan actions',
        menu_options=(
            MenuChoice(
                choice_id=MenuActionID.SELECT_BOOK,
                choice_token='e',
                choice_text='End the selected Loan'
            ),
            MenuChoice(
                choice_id=MenuActionID.GOTO_LOANS_MENU,
                choice_token='c',
                choice_text='Return to loans menu'
            ),
        )
    ),
}
