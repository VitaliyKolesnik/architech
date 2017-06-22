""" Helpers for test Model class """

def _is_username_exists(username, ulist):
    user_name = [user for user in ulist if user.user_name == username]
    return True if user_name else False

def delete_user(username, lst):
    if not _is_username_exists(username, lst):
        raise Exception("[ERROR]::There is no user with such name.")
    return [user for user in lst if user.user_name != username]

def _is_book_title_exists(book_title, lst):
    title = [book for book in lst if book.book_name == book_title]
    return True if title else False

def delete_book(title, lst):
    if not _is_book_title_exists(title, lst):
        raise Exception("[ERROR]::There is no book with shuch title.")
    return [book for book in lst if book.book_name != title]

def tbook(user, book):
    user.take_book(book)
    book.owner = user
    return user, book

def rbook(user, title, ulst, blst):
    book_index = blst.index([item for item in blst \
                            if item.book_name == title][0])
    blst[book_index].owner = None
    user_index = ulst.index([item for item in ulst \
                             if item.user_name == user][0])
    ulst[user_index].return_book(title)
    return ulst[user_index], blst[book_index]

def fback(book, rate, lst):
    index = lst.index([item for item in lst \
                      if item.book_name == book.book_name][0])
    lst[index].rate = rate
    return lst[index]
