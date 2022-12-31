# -*- coding: utf-8 -*-

"""Summary

Description
"""

from collections import deque


def camel_to_snake_case(camel_case_string: str) -> str:
    """Convert CamelCase or camelCase to snake_case.

    Preserve sequences of caps i.e:
    >>>camel_to_snake_case('CamelCase')
    'camel_case'
    >>>camel_to_snake_case('camelCase')
    'camel_case'
    >>>camel_to_snake_case('camelTMCase')
    'camel_tm_case'
    >>>camel_to_snake_case('camelCaseTM')
    'camel_case_tm'
    :param camel_case_string: source string in CamelCase or camelCase.
    :return: processed string in snake_case.
    """

    def next_snake_case_token(
            last_char: str, current_char: str = '', next_char: str = ''
    ) -> str:
        add_underscore = (
            # normal CamelCase
            (last_char.islower() and current_char.isupper())
            # Sequential caps CamelTMCase
            or (last_char.isupper()
                and current_char.isupper()
                and next_char.islower())
        )
        return (last_char + '_' if add_underscore else last_char).lower()

    snake_case_tokens = tuple(
        next_snake_case_token(*camel_case_string[index:index+3])
        for index
        in range(len(camel_case_string))
    )
    return ''.join(snake_case_tokens)


