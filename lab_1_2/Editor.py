
def find_el(cal, y, m, d):
    """Find day.
    """
    for i in cal:
        if y == i['year'] and m == i['month'] and d == i['day']:
            return i
    return None


def add_el(cal, year, month, day, teams, score, total):
    """Add element function.
    """
    i = find_el(cal, year, month, day)
    if i is None:
        day = {'year': year, 'day': day, 'month': month, 'teams': teams,
               'score': score, 'total': total}
        cal.append(day)
    else:
        print '''This day not available. Please chose another date...'''
    return cal


def del_el(cal, y, m, d):
    """Delete element function
    """
    i = find_el(cal, y, m, d)
    if i is None:
        print "This day is empty"
    else:
        cal.remove(i)
    return cal


if __name__ == "__main__":
    import doctest
    doctest.testmod()
