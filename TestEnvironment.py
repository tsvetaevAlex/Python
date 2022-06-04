from SqlWrapper import SqlWrapper
import os


class TestEnvironment:

    def __init__(self, exam_database_name):
        self.database_name = exam_database_name
        self.sql = SqlWrapper(exam_database_name)

        self.targetlist = []
        self.namelist = []
        self.enginelist = []
        self.hulllist = []
        self.weaponlist = []

    def prepare(self):
        print("going to create a ", self.database_name, "data base")
        self.sql.create_database(self.database_name)
        self.sql.create_table_ships()
        self.sql.create_table_hull()
        self.sql.create_table_weapons()
        self.sql.create_table_engines()

    def getlist(self, filename, targetlist):
        """
        :param filename: test data file
        :param targetlist: list of test data from test data file to be retuened
        :return: list of equipment names from test data files
        :rtype: list of equipment names from test data files
        """
        with open(filename) as file:
            for line in file:
                line = line.rstrip()
                self.targetlist.append(line)
                print(line)
                return targetlist

    def cleanup(self):
        print("CleanUp environment, delete outdated test database: ", self.database_name)
        print("\r\n")
        if os.path.isfile(self.database_name):
            os.remove(self.database_name)

