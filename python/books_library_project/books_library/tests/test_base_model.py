# -*- coding: utf-8 -*-

"""Summary

Description
"""

import csv
import dataclasses as dc
from unittest import TestCase

from dal.fields import (
    IntegerField, CharField, DateField, )
from dal.base_model import BaseModel, ModelError
import settings

DEMO_DATA = (
    {
        'integer_field': '1',
        'char_field': 'string 1',
        'date_field': '01/01/2000',
    },
    {
        'integer_field': '2',
        'char_field': 'string 2',
        'date_field': '02/01/2000',
    },
    {
        'integer_field': '3',
        'char_field': 'string 3',
        'date_field': '03/01/2000',
    },
)


class TestBaseModel(TestCase):
    def setUp(self):
        self.demo_model_name = 'demo_model'
        self.csv_data_file_path = settings.DATA_DIR.joinpath(
            self.demo_model_name)

        def create_test_csv_file(header_only=False):
            with open(self.csv_data_file_path, 'w', newline='') as csv_file:
                dict_writer = csv.DictWriter(
                    csv_file, DEMO_DATA[0].keys(), dialect=csv.excel_tab)
                dict_writer.writeheader()
                if header_only:
                    return
                for entry in DEMO_DATA:
                    dict_writer.writerow(entry)

        self.create_test_csv_file = create_test_csv_file

        def demo_model_factory(
        ):

            @dc.dataclass
            class DemoModel(BaseModel):
                integer_field: IntegerField = IntegerField()
                char_field: CharField = CharField()
                date_field: DateField = DateField()

            return DemoModel

        self.demo_model_factory = demo_model_factory

    def tearDown(self) -> None:
        del self.demo_model_factory
        del self.create_test_csv_file
        self.csv_data_file_path.unlink(missing_ok=True)

    def test_base_model_get_table_name(self):
        demo_model = self.demo_model_factory()
        self.assertEqual(demo_model._get_table_name(),
                         self.demo_model_name)

    def test_base_model_loads_csv_data(self):
        DemoModel = self.demo_model_factory()
        self.create_test_csv_file()
        DemoModel.load_data()
        loaded_objects = DemoModel.get_all()
        self.assertEqual(len(loaded_objects), len(DEMO_DATA))
        for entry in DEMO_DATA:
            with self.subTest(entry=entry):
                demo_object = DemoModel(**entry)
                self.assertIn(demo_object, loaded_objects)

    def test_base_model_initializes_empty_object_list_if_no_csv(self):
        DemoModel = self.demo_model_factory()
        self.assertIsNone(DemoModel.get_all())
        DemoModel.load_data()
        self.assertEqual(DemoModel.get_all(), [])

    def test_base_model_refuses_to_reload_csv_data_if_unsaved_changes(self):
        DemoModel = self.demo_model_factory()
        DemoModel.load_data()
        DemoModel.add_object(DemoModel(**DEMO_DATA[0]))
        with self.assertRaisesRegex(ModelError, r'.*reload.*'):
            DemoModel.load_data()

    def test_base_model_force_reloads_csv_data_if_unsaved_changes(self):
        DemoModel = self.demo_model_factory()
        DemoModel.load_data()
        DemoModel.add_object(DemoModel(**DEMO_DATA[0]))
        DemoModel.load_data(force=True)
        self.assertEqual(DemoModel.get_all(), [])

    def test_base_model_does_not_reload_csv_data_if_no_changes(self):
        DemoModel = self.demo_model_factory()
        self.create_test_csv_file()
        DemoModel.load_data()
        loaded_objects = DemoModel.get_all()
        self.create_test_csv_file(header_only=True)
        reloaded_objects = DemoModel.get_all()
        self.assertEqual(loaded_objects, reloaded_objects)

    def test_base_model_refuses_to_objects_of_wrong_type(self):
        DemoModel = self.demo_model_factory()
        DemoModel.load_data()
        with self.assertRaisesRegex(ModelError, r'.*object.*'):
            DemoModel.add_object(1)

    def test_base_model_writes_data_to_csv(self):
        DemoModel = self.demo_model_factory()
        DemoModel.load_data()
        for entry in DEMO_DATA:
            DemoModel.add_object(DemoModel(**entry))
        DemoModel.save_data()
        DemoModel = self.demo_model_factory()
        DemoModel.load_data()
        loaded_objects = DemoModel.get_all()
        self.assertEqual(len(loaded_objects), len(DEMO_DATA))
        for entry in DEMO_DATA:
            with self.subTest(entry=entry):
                demo_object = DemoModel(**entry)
                self.assertIn(demo_object, loaded_objects)


