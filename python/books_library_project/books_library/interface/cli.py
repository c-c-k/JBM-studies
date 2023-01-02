# -*- coding: utf-8 -*-

"""Summary

Description
"""

from enum import Enum
from typing import Callable

from interface.template import MenuTemplate, SelectionObject
from models import CustomersModel, BooksModel, LoansModel


class Menu:
    _instance = None
    _menu_templates: dict[Enum, MenuTemplate] = {}
    _menu_actions: dict[Enum, Callable] = {}
    _current_menu: MenuTemplate | None = None
    _last_menu: MenuTemplate | None = None
    _current_token_map: dict[str, Enum] | None = None
    _current_selection_map: dict[int, SelectionObject] | None = None
    _last_user_input: str | None = None
    _selected_customer: CustomersModel | None = None
    _selected_books: list[BooksModel] | None = None
    _selected_loan: LoansModel | None = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    def register_menu_action(
            self, menu_action_id: Enum, menu_action_func: Callable
    ):
        self._menu_actions[menu_action_id] = menu_action_func

    def add_menu_templates(self, menu_templates: dict[Enum, MenuTemplate]):
        self._menu_templates.update(menu_templates)

    def execute_menu_template(self, menu_id: Enum | None = None, ):
        if menu_id is not None:
            self._current_menu = self._menu_templates[menu_id]
        self._print_menu_header()
        if self._current_menu.is_custom_input_menu:
            self._print_custom_input_header()
            self._handle_custom_input()
        elif self._current_menu.is_selection_menu:
            self._print_selection_items()
            self._print_selection_header()
            self._handle_selection()
        else:
            self._build_token_map()
            self._print_menu_options()
            self._print_options_header()
            self._handle_user_choice()

    def _print_menu_header(self):
        print('=' * 72)
        print(self._current_menu.menu_path)
        print(self._current_menu.menu_header)
        if self._selected_customer:
            self._print_customer_info()
        if self._selected_books:
            self._print_books_info()
        if self._selected_loan:
            self._print_loan_info()
        print('-' * 72)

    def _print_customer_info(self):
        customer = self._selected_customer
        customer.enable_format_output()
        name = (customer.name
                if len(customer.name) < 20
                else customer.name[:20] + '...')
        city = (customer.city
                if len(customer.city) < 20
                else customer.city[:20] + '...')
        print(
            f'(loaner info: {name}, {customer.age} years old,'
            f' lives in {city})'
        )
        customer.disable_format_output()

    def _print_books_info(self):
        books = self._selected_books
        books[0].enable_format_output()
        info_header = 'books info: '
        print(info_header, end='')
        line_len = len(info_header)
        for book_info in (
            self._format_book_info(book)
            for book in books
        ):
            if line_len + len(book_info) > 72:
                print()
            line_len += len(book_info)
            print(book_info, end='; ')
        print(')')
        books[0].disable_format_output()

    @staticmethod
    def _format_book_info(book):
        name = (book.name
                if len(book.name) < 20
                else book.name[:20] + '...')
        author = (book.author
                  if len(book.author) < 20
                  else book.author[:20] + '...')
        return (
            f'({name}, by {author}, published on {book.year_published},'
            f' loan type {book.loan_type})'
        )

    def _print_loan_info(self):
        loan = self._selected_loan
        loan.enable_format_output()
        print(
            f'(loan start: {loan.loan_date}, return date {loan.return_date}'
        )
        loan.disable_format_output()

    def reset_status(self):
        self._selected_loan = None
        self._selected_customer = None
        self._selected_books = None

    def get_status(self):
        return {
            'customer': self._selected_customer,
            'books': self._selected_books,
            'loan': self._selected_loan,
        }

    def set_selection(self, object_list):
        selection_enumeration = enumerate(object_list)
        self._current_selection_map = dict(*selection_enumeration)

    def _print_selection_items(self):
        for sel_id, obj in self._current_selection_map.items():
            print(f'({sel_id}) : {obj.description}')

    def _print_selection_header(self):
        if self._last_user_input is not None:
            print('Invalid input:', self._last_user_input)
        max_selection_id = max(self._current_selection_map.keys())
        print(f'Please enter selection (1 -{max_selection_id}')
        print('(Press <CTRL-C> to cancel and return to the previous menu')

    def _handle_selection(self):
        try:
            user_input = input('>>>').strip()
        except KeyboardInterrupt:
            self._cleanup()
            self._current_menu = self._last_menu
            self.execute_menu_template()
        else:
            try:
                user_input = int(user_input)
            except (ValueError, TypeError):
                pass
            if user_input in self._current_selection_map.keys():
                selection_object = self._current_selection_map[user_input]
                action_id = self._current_menu.selection_handler_id
                self._menu_actions[action_id](selection_object)
            else:
                self._last_user_input = str(user_input)
                self.execute_menu_template()

    def _print_custom_input_header(self):
        if self._last_user_input is not None:
            print('Invalid input:', self._last_user_input)
        print(self._current_menu.custom_input_header)
        print('(Press <CTRL-C> to cancel and return to the previous menu')

    def _handle_custom_input(self):
        pattern = self._current_menu.custom_input_pattern
        try:
            user_input = input('>>>').strip()
        except KeyboardInterrupt:
            self._cleanup()
            self._current_menu = self._last_menu
            self.execute_menu_template()
        else:
            match = pattern.match(user_input)
            if match:
                action_id = self._current_menu.custom_input_handler_id
                self._menu_actions[action_id](match.groupdict())
            else:
                self._last_user_input = user_input
                self.execute_menu_template()

    def _build_token_map(self):
        self._current_token_map = {
            menu_option.choice_token: menu_option.choice_id
            for menu_option
            in self._current_menu.menu_options
        }

    def _print_menu_options(self):
        for menu_option in self._current_menu.menu_options:
            print(f'({menu_option.choice_token}) : {menu_option.choice_text}')

    def _print_options_header(self):
        if self._last_user_input is not None:
            print('Invalid input:', self._last_user_input)
        print('please select menu option: ', end='')
        print(*(f'({token})' for token in self._current_token_map))

    def _handle_user_choice(self):
        self._last_user_input = input('>>>').strip()
        if self._last_user_input in self._current_token_map:
            token = self._last_user_input
            action_id = self._current_token_map[token]
            self._last_menu = self._current_menu
            self._cleanup()
            self._menu_actions[action_id]()
        else:
            self.execute_menu_template()

    def _cleanup(self):
        self._current_token_map = None
        self._current_selection_map = None
        self._current_menu = None
        self._last_user_input = None

    def select_customer(self, customer: CustomersModel):
        self._selected_customer = customer

    def add_book_to_selection(self, book: BooksModel):
        if self._selected_books is None:
            self._selected_books = []
        self._selected_books.append(book)

    def select_loan(self, loan: LoansModel):
        self._selected_loan = loan

    @staticmethod
    def exit():
        print('Goodbye..')
