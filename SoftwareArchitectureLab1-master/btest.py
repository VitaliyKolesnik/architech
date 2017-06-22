import unittest
from unittest.mock import patch, Mock
from User import User
from Book import Book


class TestUserClass(unittest.TestCase):

    def setUp(self):
        self.book = Book('test', 'test', 2007)


    def test_getters(self):
        self.assertIsNotNone(self.book.book_name)
        self.assertIsNotNone(self.book.book_author)
        self.assertIsNotNone(self.book.book_year)


    def test_setter(self):
        new_name = 'test1'
        new_author = 'test1'
        new_year = 2008
        user = User('test', 20)
        self.book.owner = user
        self.book.book_name = new_name
        self.book.book_author = new_author
        self.book.book_year = new_year
        self.assertEqual(self.book.book_name, new_name)
        self.assertEqual(self.book.book_author, new_author)
        self.assertEqual(self.book.book_year, new_year)
        self.assertEqual(self.book.owner, user)


    def test_eq(self):
        clone = Book(self.book.book_name, self.book.book_author, self.book.book_year)
        self.assertEqual(self.book, clone)
        clone.book_name = 'reverse'
        self.assertNotEqual(self.book, clone)


    @patch('Book.Book.rate', return_value=5)
    def test_get_rate(self, rate):
        self.assertEqual(rate(), 5)

    @patch('Book.Book.owner', return_value=User('test', 11))
    def test_get_owner(self, owner):
        self.assertEqual(owner(), User('test', 11))


if __name__ == "__main__":
    unittest.main()
