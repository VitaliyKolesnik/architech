from functools import reduce
from User import *
import doctest

class Book:
    """ The class represents the enity of a real world book. """

    def __init__(self, book_name, book_author, book_year=None, rates=[]):
        """ Initializer of Book class
            Args:
                book_name:(str): The name of the book
                book_author:(str): The name of author of the current book
                book_year:(int, optional): The year when book was published

            Private attribute:
                rates:(list): The list which store all rates
                that were ever setted. Stored to compute the book's rate.

            Examples:
                >>> b = Book("Strange creatures", "Jim Salamander")
                >>> b = Book("Strange creatures", "Jim Salamander", book_year=1996)
        """
        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
        self.owner = None
        self.__rates = rates

    @property
    def book_name(self):
        """str: Property that stores the book name
            of the current book.

        Examples:
            >>> book.book_name
            'Thunderstorm'
            >>> book.book_name = "Thunderstorm: The Hammer magic"
            >>> book.book_name
            'Thunderstorm: The Hammer magic'
        """
        return self.__book_name

    @book_name.setter
    def book_name(self, book_name):
        self.__book_name = book_name

    @property
    def book_author(self):
        """str: Property that stores the book author

        Examples:
            >>> book.book_author
            'Titan'
            >>> book.book_author = "The Acient"
            >>> book.book_author
            'The Acient'
        """
        return self.__book_author

    @book_author.setter
    def book_author(self, book_author):
        self.__book_author = book_author

    @property
    def book_year(self):
        """int: Property that stores the year when the book was published.

        Examples:
            >>> book.book_year
            >>> book.book_year = 1200
            >>> book.book_year
            1200
        """
        return self.__book_year

    @book_year.setter
    def book_year(self, book_year):
        self.__book_year = book_year

    @property
    def rate(self):
        """float: The average rate of the book.
            Computing due to all rates that were ever setted
            to the current book.
        """
        return self.__rate

    @rate.setter
    def rate(self, book_rate):
        """ float: The book rate setter is computing the rate
            of book taking the sum of list with already
            setted rates and divides it on the current
            length of rates stored in rates list and plus
            one due to one added in this setter.
        """
        if (len(self.__rates) == 0):
            self.__rate = book_rate
            self.__rates.append(book_rate)
        elif (book_rate >= 0.0 and book_rate <= 5.0):
            self.__rate = (reduce(lambda x, y: x + y, self.__rates) + book_rate) / (len(self.__rates) + 1)
            self.__rates.append(book_rate)
        else:
            raise Exception('Rate value must be between 0.0 and 5.0')

    @property
    def owner(self):
        """User: The attribute of type User, that is storing
                the user, who took the book.

        Examples:
            >>> book.owner
            >>> book.owner = user
            >>> print(book.owner)
            Thor, age: 29
        """
        return self.__owner

    def _rates(self):
        return self.__rates

    @owner.setter
    def owner(self, owner):
        """ Setter checks if new value is the object of type User
        """
        if isinstance(owner, User) or owner is None:
            self.__owner = owner

    def __str__(self):
        if self.book_year:
            return "'{}', author:{}; year:{} ".format(self.book_name, \
                                               self.book_author, self.book_year)
        else:
            return "'{}', author:{};".format(self.book_name, \
                                               self.book_author)

    def __repr__(self):
        if self.book_year:
            return "'{}', author:{}; year:{} ".format(self.book_name, \
                                               self.book_author, self.book_year)
        else:
            return "'{}', author:{};".format(self.book_name, \
                                               self.book_author)


    def __eq__(self, book):
        if self.book_name == book.book_name and self.book_author == book.book_author \
        and self.book_year == book.book_year:
            return True
        return False


if __name__ == "__main__":
    doctest.testmod(extraglobs={"book": Book("Thunderstorm", "Titan"), \
                                "user": User("Thor", 29)})
