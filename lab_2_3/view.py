class View:
    """Class View for print date and calendar"""

    @staticmethod
    def out_day(cal, y, m, d):
        """Function that introduces information about a particular day"""
        flag = 0
        for i in cal:
            if y == i['year'] and m == i['month'] and d == i['day']:
                print "\n-------------------------------\nAt ", y, m, d, \
                    "\n", i['teams'], i['score'], ' total', i['total'], \
                    "\n--------------------------------"
                flag = 1
                if flag == 0:
                    print "Day not found :("



    @staticmethod
    def all_days(cal):
        """Display all days"""
        print "\n----------------------------------"
        for i in cal:
            print i['year'],  i['month'], i['day']
            print i['teams'], i['score'], i['total']
            print "----------------------------------"
