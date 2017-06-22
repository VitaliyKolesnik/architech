""" Implementation of User class """

class User:
    """ Describes all properties of library user.

    Attributes:
        __book_list(lst): Contains books are taken by a particular user.
    """

    def __init__(self, user_name, age):
        """ Initialize User class.

        Args:
            user_name(str): User name; can be an arbitrary sequence of characters.
            age(int): User's age; must be in (0..100).

        Examples:
            >>> new_user = User('Thor', 29)
            >>> new_user  #doctest: +ELLIPSIS
            <__main__.User object at 0x...>
            >>> print(new_user)
            Thor, age: 29
        """
        self.user_name = user_name
        self.age = age
        self.__book_list = []
        super().__init__()

    @property
    def user_name(self):
        """ str: Contains a name of a particular user

        Examples:
            >>> loki.user_name
            'Loki'
            >>> loki.user_name = "Loki The King of Asgard"
            >>> loki.user_name
            'Loki The King of Asgard'
        """
        return self.__user_name

    @property
    def age(self):
        """ int: Contains an age of  a particular user, must be in range(1, 100)

        Examples:
            >>> loki.age
            29
            >>> loki.age = 28
            >>> loki.age
            28
            >>> loki.age = -59
            Traceback (most recent call last):
            Exception: Age must be value between 1 and 99
        """
        return self.__age


    @property
    def book_list(self):
        """ list: Contains user's books. """
        return self.__book_list


    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            raise Exception("Age must be value between 1 and 99")

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    def take_book(self, book):
        """ Function add book to user's book list.

        Args:
            book(:obj:Book): Information about a book that user take.

        Examples:
            >>> loki.take_book(spell_book)
            >>> loki._show_book_list()
            ["'Tips and Tricks', author:The Witcher;"]
        """
        self.__book_list.append(book)

    def return_book(self, title):
        """ Remove book from the book list.

        Args:
            title(str): Book's title.

        Exapmples:
            >>> loki.return_book("Tips and Tricks")
            >>> loki._show_book_list()
            []
        """
        self.__book_list = [book for book in self.__book_list if book.book_name != title]

    def __str__(self):
        return "{}, age: {}".format(self.user_name, self.age)

    # this method created for test
    def _show_book_list(self):
        return [str(book) for book in self.book_list]

    def __eq__(self, user):
        if self.user_name == user.user_name and self.age == user.age \
        and self.book_list == user.book_list:
            return True
        return False

# I wrote this code for test
if __name__ == "__main__":
    import doctest
    from Book import Book
    doctest.testmod(extraglobs={"loki": User("Loki", 29), \
                    "spell_book": Book("Tips and Tricks", "The Witcher")})
