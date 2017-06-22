
def check_date(y, m, d=None):
    """Check correct input data.

    >>> check_date('2017', 'april', '21')
    True
    >>> check_date('1016', 'April', '21')
    False
    >>> check_date('2015', 'Apr', '21')
    False
    >>> check_date('2014', 'april', '32')
    False
    >>> check_date('2134', 'april')
    True
    >>> check_date('1996', 'oct')
    False
    """
    months = ["january", "february", "march", "april", "may", "june", "july",
              "august", "september", "october", "november", "december"]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y.isdigit() and int(y) > 1899 and int(y) < 3000:
        if m in months:
            if d is None or d.isdigit() and int(d) > 0 \
               and int(d) <= days[months.index(m)]:
                return True
    return False


def Out_day(cal, y, m, d):
    """Function that introduces information about a particular day"""
    flag = 0
    for i in cal:
        if y == i['year'] and m == i['month'] and d == i['day']:
            print "\n-------------------------------\nAt ", y, m, d, \
                "\n", i['weather'], i['temperature'], ' wimd', i['wind'], \
                "\n--------------------------------"
            flag = 1
    if flag == 0:
        print "Day not found :( Didn\'t need people being told that the"


def Temp(cal, y, m):
    """Average temperature calculation function.

    >>> cal = [{'year':'2017', 'day':'8', 'month':'march', 'weather':'sunny', 'temperature':'+13', 'wind':'3'}, {'year':'2017', 'day':'13', 'month':'march', 'weather':'sunny', 'temperature':'+20', 'wind':'3'}]
    >>> Temp(cal, '2017', 'march')
    16
    >>> Temp(cal, '2016', 'april')
    
    """
    t = d = 0
    for i in cal:
        if i['month'] == m and y == i['year']:
            t += int(i['temperature'])
            d += 1
    if d != 0:
        return (t/d)
    else:
        return None


def Midl_temp(cal):
    """Output function average temperature."""
    print "Enter year, month (example 2017 march ):"
    y = raw_input("Year = ")
    m = raw_input("Month = ")
    if check_date(y, m):
        if Temp(cal, y, m) is not None:
            print 'Average temperature in ', m, y, ' = ', Temp(cal, y, m)
        else:
            print "Data not available"
    else:
        print "Incorrect input date!"


def All_days(cal):
    """Display all days"""
    print "\n----------------------------------"
    for i in cal:
        print i['year'],  i['month'], i['day']
        print i['weather'], i['temperature'], ' wimd', i['wind'], '(m/s)'
        print "----------------------------------"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
