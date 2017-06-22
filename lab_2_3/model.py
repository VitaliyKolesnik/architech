import pickle
import serialize


class Model:
    """Class Model controls all operation on calendar."""

    def __init__(self, filename, config):
        """initialization calendar with file"""
        self.__calendar = []
        self.__filename = filename
        self.__srztype = ""
        self.__config = config
        self.__srz = serialize.Serialize()

    def setc (self, data):
        self.__calendar = data

    def load(self):
        """Load data base"""
        file_obj = open(self.__config, "r")
        self.__srztype = pickle.load(file_obj)
        file_obj.close()

        file_obj = open(self.__filename, "r")
        self.__calendar = self.__srz.load(file_obj, self.__srztype)
        file_obj.close()
            

    def save(self, srztype):
        file_obj = open(self.__filename, "w")

        if srztype == "":
            self.__srz.save(self.__calendar, file_obj, self.__srztype)
        else:
            fl = open(self.__config, "w")
            pickle.dump(srztype, fl)
            fl.close()
            self.__srz.save(self.__calendar, file_obj, srztype)
        file_obj.close()

    def find_el(self, y, m, d):
        """Find day"""
        for i in self.__calendar:
            if y == i['year'] and m == i['month'] and d == i['day']:
                return i
        return None

    def add_el(self, y, m, d, w, t, wind):
        """Add element function."""
        i = self.find_el(y, m, d)
        if i is None:
            day = {'year': y, 'day': d, 'month': m, 'weather': w,
                   'temperature': t, 'wind': wind}
            self.__calendar.append(day)
        else:
            print '''Data occupied in calendar'''

    def del_el(self, y, m, d):
        """Delete element function"""
        i = self.find_el(y, m, d)
        if i is None:
            print "This day is empty"
        else:
            self.__calendar.remove(i)

    def show(self):
        "return calendar"
        return self.__calendar

    def check_date(self, y, m, d=None):
        """Check correct input data."""
        months = ["january", "february", "march", "april", "may", "june",
                  "july", "august", "september", "october", "november",
                  "december"]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y.isdigit() and int(y) > 1899 and int(y) < 3000:
            if m in months:
                if d is None or d.isdigit() and int(d) > 0 \
                   and int(d) <= days[months.index(m)]:
                    return True
        return False

    def temp(self, y, m):
        """Average temperature calculation function."""
        t = d = 0
        for i in self.__calendar:
            if i['month'] == m and y == i['year']:
                t += int(i['temperature'])
                d += 1
        if d != 0:
            return (t/d)
        else:
            return None
