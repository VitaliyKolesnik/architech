from calendarsql import Calendar
import sqlobject


class Model:
    """Class Model controls all operation on calendar."""

    def __init__(self):
        """initialization calendar"""
        pass

    def save(self, srztype):
        if srztype != "":
            with open(".config_sql", "w") as conf:
                conf.write(srztype)

    def find_el(self, y, m, d):
        """Find day"""
        elem = list(Calendar.select(sqlobject.AND(Calendar.q.year == y,
                                                  Calendar.q.month == m,
                                                  Calendar.q.day == d)))
        if elem == []:
            return None
        return elem[0]

    def add_el(self, y, m, d, w, t, wnd):
        """Add element function."""
        if self.find_el(y, m, d) is  None:
            Calendar(year=y, month=m, day=d,
                     weather=w, temperature=t, wind=wnd)

    def del_el(self, y, m, d):
        """Delete element function"""
        elem = self.find_el(y, m, d)
        if elem is None:
            print "This day is empty"
        else:
            Calendar.delete(elem.id)

    def show(self):
        """return calendar"""
        return list(Calendar.select())

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
        elems =  list(Calendar.select(sqlobject.AND(Calendar.q.year == y,
                                                    Calendar.q.month == m)))
        
        for i in elems:
                t += int(i.temperature)
                d += 1
        if d != 0:
            return (t/d)
        else:
            return None
