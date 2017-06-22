""" Unit test for Serialize module """

from io import StringIO, BytesIO
import unittest
import pickle
import json
import yaml
from User import User
from Book import Book
import JsonSerialize as jns
import Serialize as srz


class TestSerializeMethods(unittest.TestCase):
    """ test for Serialize module """

    def setUp(self):
        user = User('test', 19)
        book = Book('test', 'author')
        user.take_book(book)
        self.data = [[user], [book]]
        self.output = None


    def test_pickle(self):
        """ test for serialization with pickle """
        output = pickle.dumps(self.data)
        self.output = BytesIO(output)
        extr_data = pickle.load(self.output)
        self.assertEqual(self.data, extr_data)


    def test_yaml(self):
        """ test for serialization with yaml """
        output = yaml.dump(self.data)
        self.output = StringIO(output)
        extr_data = yaml.load(self.output)
        self.assertEqual(self.data, extr_data)


    def test_json(self):
        """ test for serialization with json """
        output = json.dumps(self.data, default=jns.js_default)
        self.output = StringIO(output)
        users, books = srz.load(self.output, 'json')
        self.assertEqual(self.data, [users, books])

    def tearDown(self):
        self.output.close()


if __name__ == "__main__":
    unittest.main()



