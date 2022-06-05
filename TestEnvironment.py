from SqlWrapper import SqlWrapper
import configparser
import os


class TestEnvironment:
    def __init__(self) -> object:
        self.config = configparser
        self.config_filename = None
        self.environment = TestEnvironment.TestEnvironment()
        self.config = configparser.ConfigParser()
        self.config.read(self.config_filename)
        self.config = configparser.ConfigParser()
        self.config = configparser.ConfigParser()
        self.targetlist = None
        self.database_name = (self.config["EQUIPMENT"]["ShipnameListFile"])
        print(self.database_name)
        self.sql = SqlWrapper(self.config["EQUIPMENT"]["exam_database"])

    def setCongigFIleName(self, filename):
        self.config_filename = filename

    def prepare(self):
        print("going to create a ", self.database_name, "data base")
        self.sql.create_database(self.database_name)
        self.sql.create_table_ships()
        self.sql.create_table_hull()
        self.sql.create_table_weapons()
        self.sql.create_table_engines()
        self.sql.createships()
    def getlist(self, filename, targetlist):
        """
        :param filename: test data file
        :param targetlist: list of test data from test data file to be returned
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
