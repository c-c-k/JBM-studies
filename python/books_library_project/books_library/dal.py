# -*- coding: utf-8 -*-

"""Summary

Description
"""

# noinspection PyPep8Naming
import csv
import dataclasses as dc
import datetime as dt
from typing import ClassVar

import settings
import utils


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
        if hasattr(obj, '_mark_changed'):
            obj.__class__._mark_changed()


class IntegerField(BaseField):
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def _validate(self, value):
        if not isinstance(value, int):
            try:
                value = int(value)
            except (TypeError, ValueError):
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
            date = dt.datetime.strptime(value, self.date_format)
        elif isinstance(value, dt.date):
            date = value
        elif isinstance(value, dt.datetime):
            date = value.date()
        elif isinstance(value, float):
            date = dt.date.fromtimestamp(value)
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


class ModelError(Exception):
    pass


@dc.dataclass
class BaseModel:
    _objects: ClassVar[list["BaseModel"]] = None
    # TODO: figure how to implement changes detection
    _unsaved_changes: ClassVar[bool] = False

    def __post_init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    @classmethod
    def _get_table_name(cls):
        return utils.camel_to_snake_case(cls.__name__)

    @classmethod
    def load_data(cls, force=False):
        if cls._unsaved_changes and not force:
            raise ModelError('Refusing to reload data from disk '
                             'with unsaved changes in memory')
        if not cls._unsaved_changes and cls._objects:
            return
        cls._objects = []
        csv_data_file_path = settings.DATA_DIR.joinpath(cls._get_table_name())
        if not csv_data_file_path.exists():
            return
        with open(csv_data_file_path, 'r', newline='') as csv_data_file:
            dict_reader = csv.DictReader(csv_data_file, dialect=csv.excel_tab)
            for entry in dict_reader:
                cls.add_object(cls(**entry))
            cls._mark_unchanged()

    @classmethod
    def save_data(cls):
        if (
            not cls._unsaved_changes
            or not cls._objects
        ):
            return
        csv_data_file_path = settings.DATA_DIR.joinpath(cls._get_table_name())
        with open(csv_data_file_path, 'w', newline='') as csv_data_file:
            dict_writer = csv.DictWriter(
                csv_data_file,
                tuple(field.name for field in dc.fields(cls)),
                dialect=csv.excel_tab)
            dict_writer.writeheader()
            for _object in cls._objects:
                dict_writer.writerow(_object._format_for_csv())
            cls._mark_unchanged()

    def _format_for_csv(self) -> dict[str, str]:
        as_dict = dc.asdict(self)
        for key, value in as_dict.items():
            if isinstance(value, dt.date):
                as_dict[key] = value.strftime(settings.DATE_FORMAT)
            else:
                as_dict[key] = str(value)
        return as_dict

    @classmethod
    def add_object(cls, obj):
        if isinstance(obj, cls):
            cls._objects.append(obj)
        else:
            raise ModelError(
                f'{obj!r} cannot be added to objects of class {cls!r}')

    @classmethod
    def get_all(cls):
        return cls._objects

    @classmethod
    def _mark_changed(cls):
        cls._unsaved_changes = True

    @classmethod
    def _mark_unchanged(cls):
        cls._unsaved_changes = False
