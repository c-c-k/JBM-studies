import csv
import os
from pathlib import Path
import unittest

from book import Book, Books

SAMPLE_BOOK = {
    'id': 1,
    'name': 'example_book_name',
    'author': 'example_author_name',
    'year_published': 2000,
    'loan_type': 1,
}
BOOK_LOAN_TYPES = {
    'valid': [1, 2, 3],
    'invalid': [0, 4]
}
SAMPLE_BOOKS_DATASET = (
    {
        'id': 1,
        'name': 'example_book_1_name',
        'author': 'example_author_1_name',
        'year_published': 2000,
        'loan_type': 1,
    },
    {
        'id': 2,
        'name': 'example_book_2_name',
        'author': 'example_author_1_name',
        'year_published': 2001,
        'loan_type': 2,
    },
    {
        'id': 3,
        'name': 'example_book_3_name',
        'author': 'example_author_2_name',
        'year_published': 2002,
        'loan_type': 3,
    },
)


class TestBook(unittest.TestCase):
    @staticmethod
    def create_book(
            name=None, author=None, year_published=None,
            loan_type=None, id_=None
    ):
        name = name if name is not None else SAMPLE_BOOK['name']
        author = author if author is not None else SAMPLE_BOOK['author']
        year_published = (year_published if year_published is not None
                          else SAMPLE_BOOK['year_published'])
        kw_args = {}
        if loan_type is not None:
            kw_args['loan_type'] = loan_type
        if id_ is not None:
            kw_args['id_'] = id_
        return Book(name, author, year_published, **kw_args)

    def test_can_create_book_object(self):
        try:
            book_object = self.create_book()
        except (NameError, TypeError) as error:
            self.fail(f'book object creation raised {error.__class__.__name__}')

    def test_create_book_object_correct_class(self):
        book_object = self.create_book()
        self.assertIsInstance(book_object, Book)

    def test_create_book_object_base_attributes(self):
        book_object = self.create_book()
        self.assertEqual(book_object.name, SAMPLE_BOOK['name'])
        self.assertEqual(book_object.author, SAMPLE_BOOK['author'])
        self.assertEqual(book_object.year_published,
                         SAMPLE_BOOK['year_published'])

    def test_create_book_object_without_id(self):
        book_object = self.create_book()
        self.assertGreaterEqual(book_object.id, 1)

    def test_create_book_object_with_id(self):
        book_object = self.create_book(id_=999)
        self.assertEqual(book_object.id, 999)

    def test_create_book_object_with_correct_loan_type(self):
        for loan_type in BOOK_LOAN_TYPES['valid']:
            with self.subTest(loan_type=loan_type):
                try:
                    book_object = self.create_book(loan_type=loan_type)
                    self.assertEqual(book_object.loan_type, loan_type)
                except ValueError:
                    self.fail(f'loan type "1" wrongly raised ValueError')

    def test_create_book_object_with_wrong_loan_type(self):
        for loan_type in BOOK_LOAN_TYPES['invalid']:
            with self.subTest(loan_type=loan_type):
                with self.assertRaisesRegex(ValueError, '.*wrong.*type.*'):
                    book_object = self.create_book(loan_type=loan_type)


class TestBooks(unittest.TestCase):
    def setUp(self) -> None:
        test_file_path = Path('test_data_set.csv')
        with open(test_file_path, 'w', newline='') as test_data_set:
            dict_writer = csv.DictWriter(test_data_set, (
                'id', 'name', 'author', 'year_published', 'loan_type'
            ))
            dict_writer.writeheader()





if __name__ == "__main__":
    unittest.main()
