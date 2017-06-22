import unittest
from User import User
from Book import Book


class TestUserClass(unittest.TestCase):

    def setUp(self):
        self.user = User('test', 20)

    def test_getters(self):
        self.assertIsNotNone(self.user.user_name)
        self.assertIsNotNone(self.user.age)

    def test_setter(self):
        new_name = 'test1'
        new_age = 21
        self.user.user_name = new_name
        self.user.age = new_age
        self.assertEqual(self.user.user_name, new_name)
        self.assertEqual(self.user.age, new_age)
        with self.assertRaises(Exception):
            self.user.age = 100



    def test_take_remove_book(self):
        book = Book('test', 'unittest')
        self.user.take_book(book)
        self.assertNotEqual(self.user.book_list, [])
        self.user.return_book(book.book_name)
        self.assertEqual(self.user.book_list, [])

    def test_eq(self):
        clone = User(self.user.user_name, self.user.age)
        self.assertEqual(self.user, clone)
        clone.user_name = 'reverse'
        self.assertNotEqual(self.user, clone)

if __name__ == "__main__":
    unittest.main()
