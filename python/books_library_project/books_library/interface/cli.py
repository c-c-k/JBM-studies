# -*- coding: utf-8 -*-

"""Summary

Description
"""

from enum import Enum
from typing import Callable

from interface.template import MenuTemplate, SelectionObject


class Menu:
    _instance = None
    _menu_templates: dict[Enum, MenuTemplate] = {}
    _menu_actions: dict[Enum, Callable] = {}
    _current_menu: MenuTemplate | None = None
    _last_menu: MenuTemplate | None = None
    _current_token_map: dict[str, Enum] | None = None
    _current_selection_map: dict[int, SelectionObject] | None = None
    _last_user_input: str | None = None

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

    def execute_menu_template(self, menu_id: Enum | None = None,):
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
        print('-' * 72)

    def _print_selection_items(self):
        selection_enumeration = enumerate(self._current_menu.selection_items)
        self._current_selection_map = dict(*selection_enumeration)
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

    @staticmethod
    def exit():
        print('Goodbye..')
