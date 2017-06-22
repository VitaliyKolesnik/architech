
from sqlobject import *
from connectionsql import *

class Calendar(SQLObject):
    _connection = ConnectionSQL().choice_of_base()
    year = StringCol(length=4)
    month = StringCol(length=10)
    day = StringCol(length=2)
    weather = StringCol(length=100)
    temperature = StringCol(length=5)
    wind = StringCol(length=100)

    def __repr__(self):
        return "year = '{0}', month = '{1}', day = '{2}', weather = '{3}', \
temperature = '{4}', wind = '{5}'".format(self.year, self.month, self.day,
                                          self.weather, self.temperature,
                                          self.wind)

Calendar.createTable(ifNotExists=True)
