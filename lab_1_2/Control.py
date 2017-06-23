import Editor
import In_out


def mode():
    """Mode choice elements menu"""
    print "\nSelect:"
    print " 1. Show all games"
    print " 2. Find game"
    print " 3. Add game"
    print " 4. Delete game"
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
    w = raw_input('teams: ')
    t = raw_input('score: ')
    wind = raw_input('Totals("Team name" win/lose): ')
    return w, t, wind


def selector(cal, a):
    "Select enter value in mode"
    print "\nEnter year, month, day:      |example: 1995 april 20|"
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
