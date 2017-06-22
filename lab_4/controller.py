import view


class Controller:
    """Class controller for Model and View"""

    def __init__(self, calendar):
        self.__calendar = calendar

    def __mode(self):
        """Mode choice elements menu"""
        print "\nSelect:"
        print " 1. Display all days"
        print " 2. Find day"
        print " 3. Add day"
        print " 4. Delete day"
        print " 5. Rewrite day"
        print " 6. Average temperature per month"
        print "0. Exit"

        print "\nChoice: ",
        a = raw_input()

        if (not a.isdigit()) or int(a) < 0 and int(a) > 6:
            print "Input Error, try again!"
            a = self.__mode()
        return a

    def __day(self):
        """Enter date"""
        y = raw_input("Year: ")
        m = raw_input("Month: ")
        d = raw_input("Day: ")
        return y, m, d

    def __weath(self):
        """Enter weather, temperature and wimd"""
        w = raw_input('weather: ')
        t = raw_input('temperature: ')
        wind = raw_input('wimd(m/s): ')
        return w, t, wind

    def __save_result(self):
        print ("\n\nSave result as:\n1. sqlite\n2. mysql\n3. postgresql\n")
        res = int(raw_input("Select: "))
        if res == 1:
            return "sqlite"
        elif res == 2:
            return "mysql"
        elif res == 3:
            return "mysql"
        else:
            return ""

    def __selector(self, a):
        "Select enter value in mode"
        print "\nEnter year, month, day (example 2017 march 23):"
        y, m, d = self.__day()
        if self.__calendar.check_date(y, m, d):
            if int(a) == 2:
                view.View.out_day(self.__calendar.show(), y, m, d)
            if int(a) == 3:
                w, t, wind = self.__weath()
                self.__calendar.add_el(y, m, d, w, t, wind)
            if int(a) == 4:
                self.__calendar.del_el(y, m, d)
            if int(a) == 5:
                self.__calendar.del_el(y, m, d)
                w, t, wind = self.__weath()
                self.__calendar.add_el(y, m, d, w, t, wind)
        else:
            print "Incorrect input date!"

    def menu(self):
        """Main menu"""
        f = int(self.__mode())
        while f > 0 and f < 7:
            if f == 1:
                view.View.all_days(self.__calendar.show())
            elif f == 6:
                view.View.midl_temp(self.__calendar)
            else:
                self.__selector(f)
            f = int(self.__mode())
        if f == 0:
            self.__calendar.save(self.__save_result())
            return
        print "Incorrect input!"
        self.menu()
