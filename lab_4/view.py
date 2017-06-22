class View:
    """Class View for print date and calendar"""

    @staticmethod
    def out_day(cal, y, m, d):
        """Function that introduces information about a particular day"""
        flag = 0
        for i in cal:
            if y == i.year and m == i.month and d == i.day:
                print "\n-------------------------------\nAt ", y, m, d, \
                    "\n", i.weather, i.temperature, ' wimd', i.wind, \
                    "\n--------------------------------"
                flag = 1
                if flag == 0:
                    print "Day not found :("

    @staticmethod
    def midl_temp(cal):
        """Output function average temperature."""
        print "Enter year, month (example 2017 march ):"
        y = raw_input("Year = ")
        m = raw_input("Month = ")
        if cal.check_date(y, m):
            if cal.temp(y, m) is not None:
                print 'Average temperature in ', m, y, ' = ', cal.temp(y, m)
            else:
                print "Data not available"
        else:
            print "Incorrect input date!"

    @staticmethod
    def all_days(cal):
        """Display all days"""
        print "\n----------------------------------"
        for i in cal:
            print i.year,  i.month, i.day
            print i.weather, i.temperature, ' wimd', i.wind, '(m/s)'
            print "----------------------------------"
