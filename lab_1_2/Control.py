import Editor
import In_out


def mode():
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
        a = mode()
    return a


def day():
    """Enter date"""
    y = raw_input("Year: ")
    m = raw_input("Month: ")
    d = raw_input("Day: ")
    return y, m, d


def weath():
    """Enter weather, temperature and wimd"""
    w = raw_input('weather: ')
    t = raw_input('temperature: ')
    wind = raw_input('wimd(m/s): ')
    return w, t, wind


def selector(cal, a):
    "Select enter value in mode"
    print "\nEnter year, month, day (example 2017 march 23):"
    y, m, d = day()
    if In_out.check_date(y, m, d):
        if int(a) == 2:
            In_out.Out_day(cal, y, m, d)
        if int(a) == 3:
            w, t, wind = weath()
            Editor.add_el(cal, y, m, d, w, t, wind)
        if int(a) == 4:
            Editor.del_el(cal, y, m, d)
        if int(a) == 5:
            Editor.del_el(cal, y, m, d)
            Editor.add_el(cal, y, m, d)
    else:
        print "Incorrect input date!"
    return cal


def menu(cal):
    """Main menu"""
    f = int(mode())
    while f > 0 and f < 7:
        if f == 1:
            In_out.All_days(cal)
        elif f == 6:
            In_out.Midl_temp(cal)
        else:
            selector(cal, f)
        f = int(mode())
    return cal
