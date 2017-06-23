import unittest
import pickle
import model


class test_model_methods(unittest.TestCase):
    """ test for Serialize module """

    def setUp(self):
        "initialization block"
        self.data = [{'year': 1998, 'month': 'may', 'day': 12}]
        self.md = model.Model("db.txt.t", ".config.t")
        self.md.setc(self.data)

    def test_save_load(self):
        """ test for serialization with pickle """
        self.md.save('pickle')
        self.md.load()
        self.assertEqual(self.data, self.md.show())

        self.md.save('yaml')
        self.md.load()
        self.assertEqual(self.data, self.md.show())

        self.md.save('json')
        self.md.load()
        self.assertEqual(self.data, self.md.show())

        self.md.save('')
        self.md.load()
        self.assertEqual(self.data, self.md.show())

    def test_setc_show(self):
        self.md.setc(self.data)
        self.assertEqual(self.data, self.md.show())

    def test_find_el(self):
        dt = self.md.find_el('2015', 'march', '8')
        self.assertEqual(dt, None)

        self.md.setc([{'year':'2017', 'day':'8', 'month':'march', 'teams':'arsenal', 'score':'3-3', 'total':'draw'}])
        dt = self.md.find_el('2017', 'march', '8')
        self.assertEqual(dt, {'score': '3-3', 'month': 'march', 'teams': 'arsenal', 'year': '2017', 'day': '8', 'total': 'draw'})

    def test_add_el(self):
        self.md.setc([])
        dt = [{'score': '3-3', 'month': 'march', 'teams': 'arsenal', 'year': '2016', 'day': '2', 'total': 'draw'}]
        self.md.add_el('2016', 'march', '2', 'sunny', '+13', '3')
        self.assertEqual(dt, self.md.show())
        
        self.md.add_el('2016', 'march', '2', 'arsenal', '3-3', 'draw')
        self.assertEqual(dt, self.md.show())

    def test_del_el(self):
        self.md.setc([{'year':'2017', 'day':'2', 'month':'march', 'teams':'arsenal','score':'3-3', 'total':'draw'}])
        self.md.del_el("2017", "march", "2")
        self.assertEqual([], self.md.show())
        
        self.md.del_el("2017", "march", "2")
        self.assertEqual([], self.md.show())

    def test_check_date(self):
        self.assertEqual(self.md.check_date('2017', 'april', '21'), True)
        self.assertEqual(self.md.check_date('1016', 'April', '21'), False)
        self.assertEqual(self.md.check_date('2015', 'Apr', '21'), False)
        self.assertEqual(self.md.check_date('2014', 'april', '32'), False)
        self.assertEqual(self.md.check_date('2134', 'april'), True)
        self.assertEqual(self.md.check_date('1996', 'oct'), False)

    def test_temp(self):
        self.md.setc([{'year':'2017', 'day':'8', 'month':'march', 'teams':'arsenal', 'score':'3-3', 'total':'draw'},
                      {'year':'2017', 'day':'13', 'month':'march', 'teams':'arsenal', 'score':'3-3', 'total':'draw'}])
        self.assertEqual(self.md.temp('2017', 'march'), 16)
        self.assertEqual(self.md.temp('2016', 'april'), None)


        
if __name__ == "__main__":
    unittest.main()
