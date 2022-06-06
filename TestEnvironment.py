from SqlWrapper import SqlWrapper
import os
import Conf


class TestEnvironment:
    def __init__(self):

        self.config_filename = Conf.configuration_filename
        self.resultlist = []
        self.sql = SqlWrapper(self, Conf.configuration_filename)
        self.database_name = Conf.exam_database
        print(self.database_name)

    def prepare(self):
        if os.path.exists(Conf.exam_database):
            os.remove(Conf.exam_database)
        self.sql.create_database(Conf.exam_database)
        self.sql.create_table_ships()
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
        returnList = []
        if os.path.isfile(datasource_filename):
            with open(datasource_filename) as file:
                for line in file:
                    line = line.rstrip()
                    returnList.append(line)
                    print(line)
            return returnList

    def cleanup(self):
        os.remove(self.database_name)
        print("CleanUp environment, delete outdated test database: ", self.database_name)
