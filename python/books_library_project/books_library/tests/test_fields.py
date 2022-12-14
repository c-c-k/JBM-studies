# -*- coding: utf-8 -*-

"""Summary

Description
"""
import dataclasses as dc
import datetime as dt
import unittest
from unittest import TestCase

from dal.fields import (
    BaseField, IntegerField, CharField, DateField, ChoiceField,
    PrimaryKeyField, ForeignKeyField,
)
import settings


class TestCaseFields(TestCase):
    def helper_assert_equal_with_fail_on_errors(
            self, obj, field_name, input_value,
            expected_value: any = 'SAME_AS_INPUT',
            output_formatter=None,
    ):
        try:
            setattr(obj, field_name, input_value)
        except (ValueError, TypeError) as error:
            self.fail(
                '\n\tValid value flagged as invalid, '
                f'\n\tException type is: {error.__class__.__name__}'
                f'\n\tException message is: "{error.args[0]}"'
            )

        def identity(value):
            return value

        if output_formatter is None:
            output_formatter = identity
        if expected_value == 'SAME_AS_INPUT':
            expected_value = input_value
        self.assertEqual(
            output_formatter(getattr(obj, field_name)),
            expected_value
        )

    pass


class TestBaseField(TestCaseFields):
    def setUp(self):
        class DemoField(BaseField):
            pass

        class DemoClass:
            demo_field = DemoField()

        self.DemoField = DemoField
        self.DemoClass = DemoClass
        self.demo_object = DemoClass()

    def tearDown(self) -> None:
        del self.DemoField
        del self.DemoClass
        del self.demo_object

    @unittest.skip("BaseField currently doesn't have any abstract methods")
    def test_base_field_is_abstract(self):
        with self.assertRaisesRegex(TypeError, r'.+abstract.+'):
            # noinspection PyUnusedLocal
            field = BaseField()

    def test_base_field_has_default_none_value(self):
        self.assertIsNone(self.demo_object.demo_field)

    def test_base_field_reacts_to_default_value(self):
        class DemoClassWithDefault:
            demo_field_with_default = self.DemoField(1)

        self.assertEqual(
            DemoClassWithDefault().demo_field_with_default, 1)

    def test_base_field_sets_private_attribute(self):
        self.demo_object.demo_field = 1
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.demo_object._demo_field, 1)

    def test_base_field_gets_private_attribute(self):
        self.demo_object._demo_field = 1
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.demo_object.demo_field, 1)

    def test_base_field_gets_field_instance_when_called_from_owner(self):
        self.assertIsInstance(self.DemoClass.demo_field, self.DemoField)

    def test_base_field_set_reacts_to_validate(self):
        error_message = 'validation failed'
        # noinspection PyUnusedLocal
        def validate(*args, **kwargs): raise Exception(error_message)
        self.DemoField._validate = validate
        with self.assertRaisesRegex(Exception, error_message):
            self.demo_object.demo_field = 1

    def test_base_field_set_reacts_to_preprocess(self):
        # noinspection PyUnusedLocal
        def preprocess(*args, **kwargs): return 2
        self.DemoField._preprocess = preprocess
        self.demo_object.demo_field = 1
        self.assertEqual(self.demo_object.demo_field, 2)

    def test_base_field_set_reacts_to_postprocess(self):
        # noinspection PyUnusedLocal
        def postprocess(*args, **kwargs): return 2
        self.DemoField._postprocess = postprocess
        self.demo_object.demo_field = 1
        self.assertEqual(self.demo_object.demo_field, 2)

    def test_base_field_reacts_to_format_output_toggle(self):
        self.demo_object._demo_field = 1
        self.assertEqual(self.demo_object.demo_field, 1)
        self.DemoClass.demo_field.enable_format_fields_output()
        self.assertEqual(self.demo_object.demo_field, '1')
        self.DemoClass.demo_field.disable_format_fields_output()
        self.assertEqual(self.demo_object.demo_field, 1)


class TestIntegerField(TestCaseFields):
    def setUp(self):
        self.min_value = 1
        self.max_value = 3

        def demo_object_factory(
                set_min_value=False, set_max_value=False,
        ):
            kwargs = {}
            if set_min_value:
                kwargs['min_value'] = self.min_value
            if set_max_value:
                kwargs['max_value'] = self.max_value

            class DemoClass:
                demo_int_field = IntegerField(**kwargs)

            return DemoClass()

        self.demo_object_factory = demo_object_factory

    def tearDown(self) -> None:
        del self.demo_object_factory

    def test_integer_field_raises_non_integer_value(self):
        with self.assertRaisesRegex(TypeError, r'.*not.*int.*'):
            demo_object = self.demo_object_factory()
            demo_object.demo_int_field = 'non integer value'

    def test_integer_field_handles_int_castable_string(self):
        self.helper_assert_equal_with_fail_on_errors(
            obj=self.demo_object_factory(),
            field_name='demo_int_field',
            input_value='1',
            output_formatter=str,
        )

    def test_integer_field_raises_less_than_min_value(self):
        with self.assertRaisesRegex(ValueError, r'.*min.*value.*'):
            demo_object = self.demo_object_factory(set_min_value=True)
            demo_object.demo_int_field = self.min_value - 1

    def test_integer_field_raises_more_than_max_value(self):
        with self.assertRaisesRegex(ValueError, r'.*max.*value.*'):
            demo_object = self.demo_object_factory(set_max_value=True)
            demo_object.demo_int_field = self.max_value + 1

    def test_integer_field_handles_valid_values(self):
        for value in (
                self.min_value,
                self.min_value + 1,
                self.max_value,
        ):
            with self.subTest(value=value):
                self.helper_assert_equal_with_fail_on_errors(
                    obj=self.demo_object_factory(
                        set_min_value=True,
                        set_max_value=True,
                    ),
                    field_name='demo_int_field',
                    input_value=value,
                )


class TestCharField(TestCaseFields):
    def setUp(self):
        self.min_length = 1
        self.max_length = 3

        def demo_object_factory(
                set_min_length=False, set_max_length=False,
        ):
            kwargs = {}
            if set_min_length:
                kwargs['min_length'] = self.min_length
            if set_max_length:
                kwargs['max_length'] = self.max_length

            class DemoClass:
                demo_char_field = CharField(**kwargs)

            return DemoClass()

        self.demo_object_factory = demo_object_factory

    def tearDown(self) -> None:
        del self.demo_object_factory

    def test_char_field_raises_non_string_value(self):
        with self.assertRaisesRegex(TypeError, r'.*not.*str.*'):
            demo_object = self.demo_object_factory()
            demo_object.demo_char_field = 0

    def test_char_field_raises_shorter_than_min_length(self):
        with self.assertRaisesRegex(ValueError, r'.*min.*len.*'):
            demo_object = self.demo_object_factory(set_min_length=True)
            demo_object.demo_char_field = 'a' * (self.min_length - 1)

    def test_char_field_raises_longer_than_max_length(self):
        with self.assertRaisesRegex(ValueError, r'.*max.*len.*'):
            demo_object = self.demo_object_factory(set_max_length=True)
            demo_object.demo_char_field = 'a' * (self.max_length + 1)

    def test_char_field_accepts_valid_values(self):
        for value in (
                'a' * self.min_length,
                'a' * (self.min_length + 1),
                'a' * self.max_length,
        ):
            with self.subTest(value=value):
                self.helper_assert_equal_with_fail_on_errors(
                    obj=self.demo_object_factory(
                        set_min_length=True,
                        set_max_length=True,
                    ),
                    field_name='demo_char_field',
                    input_value=value,
                )


class TestDateField(TestCaseFields):
    def setUp(self):
        self.min_date = dt.datetime.now() - dt.timedelta(days=1)
        self.max_date = dt.datetime.now() + dt.timedelta(days=1)
        self.default_date_format = settings.DATE_FORMAT
        self.modified_date_format = '%d.%m.%Y'
        self.demo_datetime = dt.datetime(year=2000, month=1, day=1)
        self.default_format_date_string = self.demo_datetime.strftime(
            self.default_date_format)
        self.modified_format_date_string = self.demo_datetime.strftime(
            self.modified_date_format)

        def date_formatter_factory(default_format=True):
            _format = (self.default_date_format if default_format
                       else self.modified_date_format)

            def date_formatter(date: dt.date):
                return date.strftime(_format)

            return date_formatter

        def demo_object_factory(
                set_min_date=False, set_max_date=False,
                default_format=True
        ):
            kwargs = {}
            if set_min_date:
                kwargs['min_date'] = self.min_date
            if set_max_date:
                kwargs['max_date'] = self.max_date
            if not default_format:
                kwargs['date_format'] = self.modified_date_format

            class DemoClass:
                demo_date_field = DateField(**kwargs)

            return DemoClass()

        self.date_formatter_factory = date_formatter_factory
        self.demo_object_factory = demo_object_factory

    def tearDown(self) -> None:
        del self.demo_object_factory

    def test_date_field_raises_unimplemented_type_casting(self):
        with self.assertRaisesRegex(TypeError, r'.*cast.*'):
            demo_object = self.demo_object_factory()
            demo_object.demo_date_field = object()

    def test_date_field_raises_invalid_string_format(self):
        with self.assertRaisesRegex(ValueError, r'.*format.*'):
            demo_object = self.demo_object_factory()
            demo_object.demo_date_field = 'not a date string'

    def test_date_field_handles_default_format_date_string(self):
        self.helper_assert_equal_with_fail_on_errors(
            obj=self.demo_object_factory(),
            field_name='demo_date_field',
            input_value=self.default_format_date_string,
            output_formatter=self.date_formatter_factory(),
        )

    def test_date_field_handles_modified_format_date_string(self):
        self.helper_assert_equal_with_fail_on_errors(
            obj=self.demo_object_factory(default_format=False),
            field_name='demo_date_field',
            input_value=self.modified_format_date_string,
            output_formatter=self.date_formatter_factory(default_format=False),
        )

    def test_date_field_casts_date_from_accepted_types(self):
        for castable in (
                self.demo_datetime,
                self.demo_datetime.date(),
                self.demo_datetime.timestamp(),
        ):
            with self.subTest(castable=castable):
                self.helper_assert_equal_with_fail_on_errors(
                    obj=self.demo_object_factory(),
                    field_name='demo_date_field',
                    input_value=castable,
                    expected_value=self.default_format_date_string,
                    output_formatter=self.date_formatter_factory(),
                )

    def test_date_field_raises_earlier_than_min_date(self):
        with self.assertRaisesRegex(ValueError, r'.*min.*date.*'):
            date = self.min_date - dt.timedelta(days=1)
            demo_object = self.demo_object_factory(set_min_date=True)
            demo_object.demo_date_field = date

    def test_date_field_raises_later_than_max_date(self):
        with self.assertRaisesRegex(ValueError, r'.*max.*date.*'):
            date = self.max_date + dt.timedelta(days=1)
            demo_object = self.demo_object_factory(set_max_date=True)
            demo_object.demo_date_field = date

    def test_date_field_accepts_valid_values(self):
        date_formatter = self.date_formatter_factory()
        for date in (
                self.min_date,
                self.min_date + dt.timedelta(days=1),
                self.max_date,
        ):
            with self.subTest(date=date):
                self.helper_assert_equal_with_fail_on_errors(
                    obj=self.demo_object_factory(
                        set_min_date=True,
                        set_max_date=True,
                    ),
                    field_name='demo_date_field',
                    input_value=date,
                    expected_value=date_formatter(date),
                    output_formatter=date_formatter,
                )

    def test_date_field_reacts_to_format_output(self):
        demo_object = self.demo_object_factory()
        demo_object.__class__.demo_date_field.enable_format_fields_output()
        self.helper_assert_equal_with_fail_on_errors(
            obj=demo_object,
            field_name='demo_date_field',
            input_value=self.default_format_date_string,
        )


class TestChoiceField(TestCaseFields):
    def setUp(self):
        self.single_choice = 1
        self.multiple_choices = ('many', 'lots')
        self.invalid_choice = 3.14

        def demo_object_factory(
                set_single_choice=False,
        ):
            kwargs = {}
            if set_single_choice:
                # noinspection PyTypedDict
                kwargs['choices'] = self.single_choice
            else:
                kwargs['choices'] = self.multiple_choices

            class DemoClass:
                demo_choice_field = ChoiceField(**kwargs)

            return DemoClass()

        self.demo_object_factory = demo_object_factory

    def tearDown(self) -> None:
        del self.demo_object_factory

    def test_choice_field_handles_single_choice(self):
        self.helper_assert_equal_with_fail_on_errors(
            obj=self.demo_object_factory(set_single_choice=True),
            field_name='demo_choice_field',
            input_value=self.single_choice,
        )

    def test_choice_field_handles_multiple_choices(self):
        for value in self.multiple_choices:
            with self.subTest(value=value):
                self.helper_assert_equal_with_fail_on_errors(
                    obj=self.demo_object_factory(),
                    field_name='demo_choice_field',
                    input_value=value,
                )

    def test_choice_field_rejects_invalid_choice(self):
        with self.assertRaisesRegex(ValueError, r'.*choice.*'):
            demo_object = self.demo_object_factory()
            demo_object.demo_choice_field = self.invalid_choice


# noinspection PyPep8Naming
class TestPrimaryKeyField(TestCaseFields):
    def setUp(self):
        @dc.dataclass
        class DemoClass:
            demo_pk_field: PrimaryKeyField = PrimaryKeyField(None)

        self.DemoClass = DemoClass

    def tearDown(self) -> None:
        del self.DemoClass

    def test_pk_field_sets_next_pk_on_owner(self):
        DemoClass = self.DemoClass
        self.assertTrue(
            hasattr(DemoClass, DemoClass.demo_pk_field.last_pk_name))
        # noinspection PyUnresolvedReferences
        self.assertEqual(
            getattr(DemoClass, DemoClass.demo_pk_field.last_pk_name), 0)

    def test_pk_field_creates_new_pk_if_no_pk_provided(self):
        DemoClass = self.DemoClass
        demo_object = DemoClass()
        self.assertEqual(demo_object.demo_pk_field, 1)
        self.assertEqual(
            getattr(DemoClass, DemoClass.demo_pk_field.last_pk_name), 1)

    def test_pk_field_accepts_existing_value(self):
        DemoClass = self.DemoClass
        # noinspection PyTypeChecker
        demo_object = DemoClass(demo_pk_field='99')
        self.assertEqual(demo_object.demo_pk_field, 99)


# noinspection PyTypeChecker
class TestForeignKeyField(TestCaseFields):
    def setUp(self):
        @dc.dataclass
        class DemoForeignClass:
            demo_pk_field: PrimaryKeyField = PrimaryKeyField()

        @dc.dataclass
        class DemoClass:
            demo_fk_field: ForeignKeyField = ForeignKeyField(DemoForeignClass)

        self.DemoForeignClass = DemoForeignClass
        self.DemoClass = DemoClass

    def tearDown(self) -> None:
        del self.DemoClass
        del self.DemoForeignClass

    # noinspection PyUnusedLocal
    def test_fk_field_refuses_non_dataclass(self):
        class DemoForeignClass:
            demo_pk_field: PrimaryKeyField = PrimaryKeyField()

        with self.assertRaisesRegex(TypeError, r'.*dataclass.*'):
            @dc.dataclass
            class DemoClass:
                demo_fk_field: ForeignKeyField = ForeignKeyField(
                    DemoForeignClass)

    # noinspection PyUnusedLocal
    def test_fk_field_refuses_classes_without_pk(self):
        @dc.dataclass
        class DemoForeignClass:
            pass

        with self.assertRaisesRegex(AttributeError, r'.*p.*k.*'):
            @dc.dataclass
            class DemoClass:
                demo_fk_field: ForeignKeyField = ForeignKeyField(
                    DemoForeignClass)

    def test_fk_field_set_accepts_foreign_class(self):
        foreign_object = self.DemoForeignClass('99')
        demo_object = self.DemoClass(foreign_object)
        self.assertIs(demo_object.demo_fk_field, foreign_object)

    def test_fk_field_set_accepts_foreign_pk(self):
        foreign_object = self.DemoForeignClass('99')
        def get_all(): return [foreign_object]
        self.DemoForeignClass.get_all = get_all
        demo_object = self.DemoClass('99')
        self.assertIs(demo_object.demo_fk_field, foreign_object)

    def test_fk_field_reacts_to_format_toggle(self):
        foreign_object = self.DemoForeignClass('99')
        demo_object = self.DemoClass(foreign_object)
        self.DemoClass.demo_fk_field.enable_format_fields_output()
        self.assertEqual(demo_object.demo_fk_field, '99')
