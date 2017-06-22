import unittest
from model import *


class test_serialize_methods(unittest.TestCase):
    """ test for Serialize module """

    def setUp(self):        
        self.__md = Model()

    def test_save(self):
        tp = 'mysql'
        self.__md.show()
        self.__md.save(tp)
        with open(".config_sql", "r") as conf:
            self.assertEqual(tp, conf.readline())
        
    def test(self):
        el = "year = '{0}', month = '{1}', day = '{2}', weather = '{3}', \
temperature = '{4}', wind = '{5}'".format('1997', 'may', '5', 'sunny', '+23', '3')
        self.__md.add_el('1997', 'may', '5', 'sunny', '+23', '3')
        res = "{0}".format(self.__md.find_el('1997', 'may', '5'))
        self.assertEqual(el, res)

        self.__md.del_el('1997', 'may', '5')
        res = self.__md.find_el('1997', 'may', '5')
        self.assertEqual(None, res)
        
        self.__md.del_el('1997', 'may', '5')
        res = self.__md.find_el('1997', 'may', '5')
        self.assertEqual(None, res)

    def test_check_date(self):
        self.assertEqual(self.__md.check_date('2017', 'april', '21'), True)
        self.assertEqual(self.__md.check_date('1016', 'April', '21'), False)
        self.assertEqual(self.__md.check_date('2015', 'Apr', '21'), False)
        self.assertEqual(self.__md.check_date('2014', 'april', '32'), False)
        self.assertEqual(self.__md.check_date('2134', 'april'), True)
        self.assertEqual(self.__md.check_date('1996', 'oct'), False)

    def test_temp(self):
        res = self.__md.temp('2013', 'may')
        self.assertEqual(res, 13)
        
        res = self.__md.temp('1996', 'november')
        self.assertEqual(res, None)
    

if __name__ == "__main__":
    unittest.main()
