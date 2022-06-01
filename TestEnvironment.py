import SqlWrapper


class TestEnvironment:

    def __init__(self, exam_database_name):
        self.sql = SqlWrapper
        self.database_name = exam_database_name

    def prepare(self):
        print("going to create a ", self.database_name, "data base")
        self.sql.create_database(self.database_name)
        self.sql.create_table_ships()
        self.sql.create_table_hulls()
        self.sql.create_table_weapons()
        self.sql.create_table_engines()

    def create_database(self):
        print("inside: create_database")

    def create_table_ships(self):
        print("inside: create_table_ships")

    def create_table_hulls(self):
        print("inside: create_table_hulls")

    def create_table_weapons(self):
        print("inside: create_table_weapons")

    def create_table_engines(self):
        print("inside: create_table_engines")
