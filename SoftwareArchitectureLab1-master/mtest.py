""" Tests for Model class """

import unittest
from unittest.mock import patch
from User import User
from Book import Book
import test_helpers as th


class TestModelClass(unittest.TestCase):

    @patch('Model.Model')
    def test_user_book_create(self, Model):
        model = Model()
        model.user_list.return_value = [User('test', 11)]
        model.book_list.return_value = [Book('test', 'test')]
        ulist = model.user_list()
        blist = model.book_list()
        self.assertNotEqual(ulist, [])
        self.assertNotEqual(blist, [])

    @patch('Model.Model.remove_user', side_effect=th.delete_user)
    def test_remove_user(self, remove_user):
        self.assertEqual(remove_user('test', [User('test', 11)]), [])
        with self.assertRaises(Exception):
            remove_user('t', [User('test', 11)])

    @patch('Model.Model.remove_book', side_effect=th.delete_book)
    def test_remove_book(self, remove_book):
        self.assertEqual(remove_book('test', [Book('test', 'test')]), [])
        with self.assertRaises(Exception):
            remove_book('t', [Book('test', 'test')])

    @patch('Model.Model.take_book', side_effect=th.tbook)
    def test_take_book(self, take_book):
        user = User('test', 11)
        book = Book('test', 'test')
        user, book = take_book(user, book)
        self.assertEqual(user.book_list[0], book)
        self.assertEqual(book.owner, user)

    @patch('Model.Model.return_book', side_effect=th.rbook)
    def test_return_book(self, return_book):
        user = User('test', 11)
        book = Book('test', 'test')
        user, book = th.tbook(user, book)
        user, book = return_book(user.user_name, book.book_name, [user], [book])
        self.assertEqual(user.book_list, [])
        self.assertEqual(book.owner, None)

    @patch('Model.Model.feedback', side_effect=th.fback)
    def test_feedback(self, feedback):
        lst = [Book('test', 'test1', rates=[2, 3]), Book('test1', 'test1')]
        book = feedback(Book('test', 'test1', rates=[2, 3]), 1, lst)
        self.assertEqual(book.rate, 2)


if __name__ == "__main__":
    unittest.main()
