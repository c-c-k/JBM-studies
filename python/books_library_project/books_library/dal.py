# -*- coding: utf-8 -*-

"""Summary

Description
"""

# noinspection PyPep8Naming
from datetime import datetime as DateTime, date as Date

import settings


class BaseField:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, obj_type=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if hasattr(self, '_preprocess'):
            value = self._preprocess(value)
        if hasattr(self, '_validate'):
            self._validate(value)
        if hasattr(self, '_postprocess'):
            value = self._postprocess(value)
        setattr(obj, self.private_name, value)


class IntegerField(BaseField):
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def _validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'{value} is not an integer.')
        if (
                (self.min_value is not None)
                and (value < self.min_value)
        ):
            raise ValueError(f'{value} is less than the minimal allowed '
                             f'value {self.min_value}')
        if (
                (self.max_value is not None)
                and (value > self.max_value)
        ):
            raise ValueError(f'{value} is greater than the maximal allowed '
                             f'value {self.max_value}')


class CharField(BaseField):
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def _validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'{value} is not a string.')
        if (
                (self.min_length is not None)
                and (len(value) < self.min_length)
        ):
            raise ValueError(f'length of {value} is less than the minimal '
                             f'allowed length {self.min_length}')
        if (
                (self.max_length is not None)
                and (len(value) > self.max_length)
        ):
            raise ValueError(f'length of {value} is greater than the maximal '
                             f'allowed length {self.max_length}')


class DateField(BaseField):
    def __init__(
            self, date_format=settings.DATE_FORMAT,
            min_date=None, max_date=None
    ):
        self.date_format = date_format
        self.min_date = (
            self._cast_to_date(min_date)
            if min_date is not None
            else None
        )
        self.max_date = (
            self._cast_to_date(max_date)
            if max_date is not None
            else None
        )

    def _cast_to_date(self, value):
        if isinstance(value, str):
            date = DateTime.strptime(value, self.date_format)
        elif isinstance(value, Date):
            date = value
        elif isinstance(value, DateTime):
            date = value.date()
        elif isinstance(value, float):
            date = Date.fromtimestamp(value)
        else:
            raise TypeError((
                f'date type casting from {type(value)} is not supported '
                f' (input raw_date is{value}).'
            ))
        return date

    def _preprocess(self, value):
        return self._cast_to_date(value)

    def _validate(self, value):
        date = value
        if (
                (self.min_date is not None)
                and (date < self.min_date)
        ):
            raise ValueError(f'{date} is earlier than the minimal '
                             f'allowed date of {self.min_date}')
        if (
                (self.max_date is not None)
                and (date > self.max_date)
        ):
            raise ValueError(f'{date} is later than the maximal '
                             f'allowed date of {self.max_date}')


class ChoiceField(BaseField):
    def __init__(self, choices):
        try:
            self.choices = set(choices)
        except TypeError:
            self.choices = {choices}

    def _validate(self, value):
        if value not in self.choices:
            raise ValueError(
                f'{value} is not one of the valid choices of{self.choices}'
            )
