# -*- coding: utf-8 -*-

"""Summary

Description
"""

import csv
import datetime as dt
from pathlib import Path
from pprint import pprint
from random import randint


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
        next_snake_case_token(*camel_case_string[index:index + 3])
        for index
        in range(len(camel_case_string))
    )
    return ''.join(snake_case_tokens)


BOOK_SOURCE = Path('./data/classics.csv')
BOOK_FILTERED = Path('./data/demo_books_model.csv')
CLIENT_SOURCE = Path('./data/customers-100.csv')
CLIENT_FILTERED = Path('./data/demo_customers_model.csv')
LOAN_DATA = Path('./data/demo_loans_model.csv')


def pprint_source_csv_headers(csv_file: Path):
    with open(csv_file, 'r', newline='') as csv_io:
        csv_dict = csv.DictReader(csv_io)
        pprint(next(csv_dict))


def extract_book_data():
    def is_invalid_entry(entry: dict):
        name = entry['name']
        return (',' in name) or (';' in name)

    def filter_book_entry(source_entry_: dict) -> dict:
        return {
            'name': source_entry_['bibliography.title'],
            'author': source_entry_['bibliography.author.name'].replace(',',
                                                                        ' '),
            'year_published': source_entry_['bibliography.publication.year'],
        }

    with open(BOOK_SOURCE, 'r', newline='') as source:
        with open(BOOK_FILTERED, 'w', newline='') as filtered:
            csv_dict_reader = csv.DictReader(source)
            csv_dict_writer = csv.DictWriter(
                f=filtered,
                fieldnames=('id', 'name', 'author',
                            'year_published', 'loan_type'),
                dialect=csv.excel_tab,
            )
            csv_dict_writer.writeheader()
            for book_id in range(1, 101):
                source_entry = next(csv_dict_reader)
                filtered_entry = filter_book_entry(source_entry)
                while is_invalid_entry(filtered_entry):
                    source_entry = next(csv_dict_reader)
                    filtered_entry = filter_book_entry(source_entry)
                filtered_entry['id'] = str(book_id)
                filtered_entry['loan_type'] = str(randint(1, 3))
                csv_dict_writer.writerow(filtered_entry)


def extract_client_data():
    with open(CLIENT_SOURCE, 'r', newline='') as source:
        def filter_client_entry(_source_entry: dict) -> dict:
            return {
                'name': ' '.join((
                    _source_entry['First Name'],
                    _source_entry['Last Name'])),
                'city': _source_entry['City'],
            }

        with open(CLIENT_FILTERED, 'w', newline='') as filtered:
            csv_dict_reader = csv.DictReader(source)
            csv_dict_writer = csv.DictWriter(
                f=filtered,
                fieldnames=('id', 'name', 'city', 'age'),
                dialect=csv.excel_tab,
            )
            csv_dict_writer.writeheader()
            for id_ in range(1, 101):
                source_entry = next(csv_dict_reader)
                filtered_entry = filter_client_entry(source_entry)
                filtered_entry['id'] = str(id_)
                filtered_entry['age'] = str(randint(6, 120))
                csv_dict_writer.writerow(filtered_entry)


def gen_loan_data():
    date_format = '%d/%m/%Y'

    def gen_loan_date(
            base: dt.datetime = dt.datetime.now()
    ) -> dt.datetime:
        recent = randint(1, 100) <= 60  # 60% chance for a recent loan
        if recent:
            offset = dt.timedelta(days=randint(1, 7))
        else:
            offset = dt.timedelta(weeks=randint(2, 200))
        return base - offset

    def gen_return_date(
            loan_date_: dt.datetime
    ) -> dt.datetime:
        offset = dt.timedelta(days=randint(1, 14))
        _return_date = loan_date_ + offset
        return ( _return_date
                 if _return_date < dt.datetime.now()
                 else None)

    with open(LOAN_DATA, 'w', newline='') as loans_file:
        csv_dict_writer = csv.DictWriter(
            f=loans_file,
            fieldnames=('customer_id', 'book_id', 'loan_date', 'return_date'),
            dialect=csv.excel_tab,
        )
        csv_dict_writer.writeheader()
        for _ in range(100):
            loan_date = gen_loan_date()
            return_date = gen_return_date(loan_date)
            entry = {
                'customer_id': str(randint(1, 100)),
                'book_id': str(randint(1, 100)),
                'loan_date': loan_date.strftime(date_format),
                'return_date': (return_date.strftime(date_format)
                                if return_date is not None
                                else '')
            }
            csv_dict_writer.writerow(entry)


def identity_func(obj):
    return obj
