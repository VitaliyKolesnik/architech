""" Module for serialization using JSON format """

import json
from User import User
from Book import Book

def js_default(obj):
    """ serialize method for User and Book classes"""
    if isinstance(obj, Book):
        return dict([('book_name', obj.book_name), ('book_author', obj.book_author), \
                    ('book_year', obj.book_year), ('rates', obj._rates())])
    elif isinstance(obj, User):
        return dict([('user_name', obj.user_name), ('age', obj.age), ('book_list', obj.book_list)])



def decode(lst):
    """ Decode serialized data """
    user_list, book_list = lst
    users = list()
    book_list = [Book(book['book_name'], book['book_author'], book['book_year'], book['rates']) \
                for book in book_list]

    for record in user_list:
        user = User(record['user_name'], record['age'])
        for item in record['book_list']:
            book = Book(item['book_name'], item['book_author'], item['book_year'], item['rates'])
            book_list[book_list.index(book)].owner = user
            book.owner = user
            user.take_book(book)
        users.append(user)
    return users, book_list

def jload(file_obj):
    """ Load model from a file """
    data = json.load(file_obj)
    user_list, book_list = decode(data)
    return user_list, book_list

def jdump(data, file_obj):
    """ Dump model to a file """
    json.dump(data, file_obj, default=js_default)

