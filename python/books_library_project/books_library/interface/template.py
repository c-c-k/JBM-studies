# -*- coding: utf-8 -*-

"""Summary

Description
"""

import dataclasses as dc
from enum import Enum
from typing import NamedTuple, Pattern


@dc.dataclass
class MenuChoice:
    choice_id: Enum
    choice_token: str
    choice_text: str


@dc.dataclass
class SelectionObject:
    object: object
    description: str


class MenuTemplate(NamedTuple):
    menu_id: Enum
    menu_path: str
    menu_options: tuple[MenuChoice, ...] = None
    menu_header: str = 'Welcome to the books library.'
    is_selection_menu: bool = False
    selection_items: list[SelectionObject] = None
    selection_handler_id: Enum = None
    is_custom_input_menu: bool = False
    custom_input_header: str = None
    custom_input_pattern: Pattern = None
    custom_input_handler_id: Enum = None
