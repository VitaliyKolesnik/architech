from io import StringIO, BytesIO
import unittest
import pickle
import json
import yaml
import serialize as srz


class test_serialize_methods(unittest.TestCase):
    """ test for Serialize module """

    def setUp(self):
        "initialization block"
        self.data = [{'year': 1998, 'month': 'may', 'day': 12}]
        self.output = None

    def test_pickle(self):
        """ test for serialization with pickle """
        output = srz.save(self.data, self.output, 'pickle')
        self.output = BytesIO(output)
        extr_data = srz.load(self.output, "pickle")
        self.assertEqual(self.data, extr_data)

    def test_yaml(self):
        """ test for serialization with yaml """
        output = srz.save(self.data, self.output, 'yaml')
        output = unicode(output)
        self.output = StringIO(output)
        extr_data = srz.load(self.output, 'yaml')
        self.assertEqual(self.data, extr_data)

    def test_json(self):
        """ test for serialization with json """
        output = srz.save(self.data, self.output, 'json')
        output = unicode(output)
        self.output = StringIO(output)
        extr_data = srz.load(self.output, 'json')
        self.assertEqual(self.data, extr_data)

    def tearDown(self):
        self.output.close()


if __name__ == "__main__":
    unittest.main()
