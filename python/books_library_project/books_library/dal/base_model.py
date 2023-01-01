# -*- coding: utf-8 -*-

"""Summary

Description
"""
import csv
import dataclasses as dc
from typing import ClassVar

import settings
import utils


class ModelError(Exception):
    pass


@dc.dataclass
class BaseModel:
    _objects: ClassVar[list["BaseModel"]] = None
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
            cls.mark_unchanged()

    @classmethod
    def enable_format_output(cls):
        for field in dc.fields(cls):
            getattr(cls, field.name).enable_format_fields_output()

    @classmethod
    def disable_format_output(cls):
        for field in dc.fields(cls):
            getattr(cls, field.name).disable_format_fields_output()

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
            cls.enable_format_output()
            for _object in cls._objects:
                dict_writer.writerow(dc.asdict(_object))
            cls.disable_format_output()
            cls.mark_unchanged()

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
    def mark_changed(cls):
        cls._unsaved_changes = True

    @classmethod
    def mark_unchanged(cls):
        cls._unsaved_changes = False
