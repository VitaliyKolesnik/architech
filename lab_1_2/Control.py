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

    if (not a.isdigit()) or int(a) < 0 and int(a) > 4:
        print "Input Error, try again!"
        a = mode()
    return a


def date():
    """Enter date"""
    year = raw_input("Year: ")
    month = raw_input("Month: ")
    day = raw_input("Day: ")
    return year, month, day


def match():
    """Enter teams, score and team_name"""
    team = raw_input('teams: ')
    score = raw_input('score: ')
    total = raw_input('Totals("Team name" win/lose): ')
    return team, score, total


def selector(cal, a):
    "Select enter value in mode"
    print "\nEnter year, month, day:      |example: 1995 april 20|"
    year, month, day = date()
    if In_out.check_date(year, month, day):
        if int(a) == 2:
            In_out.Out_day(cal, year, month, day)
        if int(a) == 3:
            team, score, total = match()
            Editor.add_el(cal, year, month, day, team, score, total)
        if int(a) == 4:
            Editor.del_el(cal, year, month, day)
    else:
        print "Incorrect input date!"
    return cal


def menu(cal):
    """Main menu"""
    f = int(mode())
    while f > 0 and f < 6:
        if f == 1:
            In_out.All_days(cal)
        else:
            selector(cal, f)
        f = int(mode())
    return cal
