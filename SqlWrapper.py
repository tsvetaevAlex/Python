import sqlite3
from sqlite3 import Error
imnport DataDump

class SqlWrapper:

    def __init__(self, test_db_name):
        self.dataDump = DataDump

        self.cursor = None
        self.dbConnection = None
        self.testDb = test_db_name

    def create_database(self, test_db_name):
        print("there, we wil prepare our test data base, let`s do it.")
        try:
            self.dbConnection = sqlite3.connect(test_db_name)
            self.cursor = self.dbConnection.cursor()
        except Error:
            print(Error)

    def create_table_ships(self):
        print("we are in create_table_ship")
        self.cursor.execute("create table Ships(ship text NOT NULL PRIMARY KEY,weapon text[not NULL], hull text[NOT "
                            + "NULL]engine text[not NULL]);")

    def create_table_hull(self):
        print("we are in create_table_hull")
        self.cursor.execute("create table Hull(ship text NOT NULL PRIMARY KEY,hull text [not NULL], armor int [NOT "
                            + "NULL]ArmorType int[not NULL]capacity int[not NULL]);")

    def create_table_weapons(self):
        print("we are create_table_weapon")
        self.cursor.execute("create  table Weapons(weapon text NOT NULL Primary KEY,reloadSpeed int[not NULL] range "
                            + "text[not NULL], powerVolley text[not NULL]count text[not NULL]);")

    def create_table_engines(self):
        print("we are in create_table_engine")
        self.cursor.execute("create table Engine(engine text NOT NULL PRIMARY KEY,EnginePower int [not NULL], "
                            + "EngineType int [not NULL]);")

        self.dbConnection.commit()

    def createship(self):
        weapon = self.environment.weaponlist
        hull = self

        print("get lucky with fill up our database let the magic begin.")

        self.cursor.execute()

