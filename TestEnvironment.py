from SqlWrapper import SqlWrapper
import configparser
import os
import main
import DataDump


class TestEnvironment:
    def __init__(self):

        self.config = configparser
        self.environment = TestEnvironment()
        self.config = configparser.ConfigParser()
        self.config.read(main.configuration_filename)
        self.config = configparser.ConfigParser()
        self.config = configparser.ConfigParser()
        self.config_filename = main.configuration_filename
        self.sql = SqlWrapper(self.config_filename)
        self.resultlist = []
        self.database_name = main.exam_database
        print(self.database_name)

    def prepare(self):
        self.database_name = main.exam_database
        self.sql.create_database(main.configuration_filename)
        self.sql.create_table_ships()
        self.sql.create_table_hulls()
        self.sql.insert_hull_details()
        self.sql.create_table_weapons()
        self.sql.insert_weapon_details()
        self.sql.create_table_engines()
        self.sql.insert_engine_details()
        self.sql.create_table_hulls()
        self.sql.insert_hull_details()

        self.sql.BattleShips_CreateARmada()

    def getList_fromfile(self, datasource_filename):
        """
        :param datasource_filename: test data file
        """
        if os.path.isfile(self.database_name):
            with open(datasource_filename) as file:
                for line in file:
                    line = line.rstrip()
                    self.resultlist.append(line)
                    print(line)
            return self.resultlist

    def cleanup(self):
        os.remove(self.database_name)
        print("CleanUp environment, delete outdated test database: ", self.database_name)
