import unittest

import book

SAMPLE_BOOK = {
    'name': 'example_book_name',
    'author': 'example_author_name',
    'year_published': 2000,
}
BOOK_LOAN_TYPES = {
    'valid': [1, 2, 3],
    'invalid': [0, 4]
}


class TestBook(unittest.TestCase):
    def create_book(self, loan_type=None, id_=None):
        from book import Book
        return Book(
            SAMPLE_BOOK['name'],
            SAMPLE_BOOK['author'],
            SAMPLE_BOOK['year_published'],
        )

    def test_create_book_object(self):
        try:
            book = self.create_book()
        except (NameError, TypeError) as error:
            self.fail(f'book object creation raised {error.__class__.__name__}')




if __name__ == "__main__":
    unittest.main()
