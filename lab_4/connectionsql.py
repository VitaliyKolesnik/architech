import os
import sqlobject

class ConnectionSQL:
    """Class ConnectionSQL for connection to MySQL SQLite PostGreSQL"""

    def __read_config_sql(self):
        """read .config_sql"""
        with open(".config_sql", "r") as conf:
            for line in conf:
                if line[0] != '#':
                    return line

    def choice_of_base(self):
        base = self.__read_config_sql()
        path = ""
        if base == "sqlite":
            path = "sqlite:" + os.path.abspath("data.db")
        elif base == "mysql":
            path = "mysql://root:1111@127.0.0.1/vpdb"
        elif base == "postgresql":
            path = "mysql://test:www@127.0.0.1/sammy"
        else:
            raise Exception("" + base + " doesn't exist ")

        return sqlobject.connectionForURI(path)

