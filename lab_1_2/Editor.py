
def find_el(cal, y, m, d):
    """Find day.

    >>> find_el([], '2015', 'march', '8')
    
    >>> cal = [{'year':'2017', 'day':'8', 'month':'march', 'weather':'sunny', 'temperature':'+13', 'wind':'3'}]
    >>> find_el(cal, '2017', 'march', '8')
    {'temperature': '+13', 'month': 'march', 'weather': 'sunny', 'year': '2017', 'day': '8', 'wind': '3'}
    """
    for i in cal:
        if y == i['year'] and m == i['month'] and d == i['day']:
            return i
    return None


def add_el(cal, y, m, d, w, t, wind):
    """Add element function.
    
    >>> add_el([], '2016', 'march', '2', 'sunny', '+13', '3')
    [{'temperature': '+13', 'month': 'march', 'weather': 'sunny', 'year': '2016', 'day': '2', 'wind': '3'}]
    >>> cal = [{'temperature': '+13', 'month': 'march', 'weather': 'sunny', 'year': '2016', 'day': '2', 'wind': '3'}]
    >>> add_el(cal, '2016', 'march', '2', 'sunny', '+13', '3')
    This day already have an input if you want to change select the editing mode
    [{'temperature': '+13', 'month': 'march', 'weather': 'sunny', 'year': '2016', 'day': '2', 'wind': '3'}]
    """
    i = find_el(cal, y, m, d)
    if i is None:
        day = {'year': y, 'day': d, 'month': m, 'weather': w,
               'temperature': t, 'wind': wind}
        cal.append(day)
    else:
        print '''This day already have an input if you want \
to change select the editing mode'''
    return cal


def del_el(cal, y, m, d):
    """Delete element function
    >>> cal =  [{'year':'2017', 'day':'2', 'month':'march', 'weather':'sunny','temperature':'+13', 'wind':'3'}]
    >>> del_el(cal, "2017", "march", "2")
    []
    >>> del_el(cal, "2017", "march", "2")
    This day is empty
    []
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
