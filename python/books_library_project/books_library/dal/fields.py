# -*- coding: utf-8 -*-

"""Summary

Description
"""

# noinspection PyPep8Naming
import dataclasses as dc
import datetime as dt

import settings


class BaseField:

    def __init__(self, default=None):
        self.format_output_active = False
        self._default = default

    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
        self._name = '_' + name

    def enable_format_fields_output(self):
        self.format_output_active = True

    def disable_format_fields_output(self):
        self.format_output_active = False

    # noinspection PyMethodMayBeStatic
    def format_output(self, value):
        return str(value)

    def __get__(self, obj, obj_type=None):
        if obj is None:
            value = self
        else:
            value = getattr(obj, self._name, self._default)
            if self.format_output_active:
                value = self.format_output(value)
        return value

    def __set__(self, obj, value):
        if hasattr(self, '_preprocess'):
            value = self._preprocess(value)
        if hasattr(self, '_validate'):
            self._validate(value)
        if hasattr(self, '_postprocess'):
            value = self._postprocess(value)
        setattr(obj, self._name, value)
        if hasattr(obj, 'mark_changed'):
            obj.__class__.mark_changed()


class IntegerField(BaseField):
    def __init__(self, min_value=None, max_value=None, default=None):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(default)

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
    def __init__(self, min_length=None, max_length=None, default=None):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(default)

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
            min_date=None, max_date=None, default=None
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
        super().__init__(default)

    def format_output(self, value):
        return dt.date.strftime(value, self.date_format)

    def _cast_to_date(self, value):
        if isinstance(value, str):
            if value == '':
                date = None
            else:
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
        if value is None:
            return
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
    def __init__(self, choices, default=None):
        try:
            self.choices = set(choices)
        except TypeError:
            self.choices = {choices}
        super().__init__(default)

    def _validate(self, value):
        if value not in self.choices:
            raise ValueError(
                f'{value} is not one of the valid choices of{self.choices}'
            )


class PrimaryKeyField(BaseField):
    last_pk_name = '_last_primary_key'

    def __set_name__(self, owner, name):
        super().__set_name__(owner, name)
        setattr(owner, self.last_pk_name, 0)

    def update_last_pk(self, next_pk):
        setattr(self.owner, self.last_pk_name, next_pk)

    def _preprocess(self, value):
        if value is self:
            pk = getattr(self.owner, self.last_pk_name) + 1
            self.update_last_pk(pk)
        else:
            pk = int(value)
        return pk


class ForeignKeyField(BaseField):
    def __init__(self, foreign_class, default=None):
        super().__init__(default)
        if not dc.is_dataclass(foreign_class):
            raise TypeError("ForeignKey field can only handle dataclasses.")
        for field in dc.fields(foreign_class):
            if field.type is PrimaryKeyField:
                self.foreign_class_pk_field_name = field.name
                break
        else:
            raise AttributeError("Can't create foreign key for "
                                 f"class {foreign_class!r} as it doesn't "
                                 f"have a primary key.")
        self.foreign_class = foreign_class

    def format_output(self, value):
        return str(getattr(value, self.foreign_class_pk_field_name))

    def _preprocess(self, value):
        if not isinstance(value, self.foreign_class):
            foreign_pk = int(value)
            for obj in self.foreign_class.get_all():
                if (
                        dc.asdict(obj)[self.foreign_class_pk_field_name]
                        == foreign_pk
                ):
                    value = obj
                    break
            else:
                raise ValueError(f'foreign key {foreign_pk} not found '
                                 f'in {self.foreign_class} objects '
                                 'collection.')
        return value
