from SqlWrapper import SqlWrapper


class TestEnvironment:

    def __init__(self, exam_database_name):
        self.database_name = exam_database_name
        self.sql = SqlWrapper("BattleShips_exam.db")

    def prepare(self):
        print("going to create a ", self.database_name, "data base")
        self.sql.create_database(self.database_name)
        self.sql.create_table_ships()
        self.sql.create_table_hull()
        self.sql.create_table_weapons()
        self.sql.create_table_engines()
