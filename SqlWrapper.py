import sqlite3
from sqlite3 import Error
import DataDump


class SqlWrapper:

    def __init__(self, test_db_name):
        self.datadump = DataDump.DataDump()
        self.names = self.datadump.namelist
        self.cursor = None
        self.dbConnection = None
        self.testDb = test_db_name
        self.sqlParamShipName = self.datadump.get_shipname()
        self.sqlParamHull = self.datadump.get_hull()
        self.sqlParamWeapon = self.datadump.get_weapon()
        self.sqlParamEngine = self.datadump.get_engine()

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
                            + "NULL], engine text[not NULL]);")

    def create_table_hull(self):
        print("we are in create_table_hull")
        self.cursor.execute("create table Hull(hull text [not NULL], armor int " +
                            "[NOT NULL]ArmorType int[not NULL]capacity int[not NULL]);")

    def create_table_weapons(self):
        print("we are create_table_weapon")
        self.cursor.execute("create  table Weapons(weapon text NOT NULL Primary KEY,reloadSpeed int[not NULL] range "
                            + "int [not NULL], powerVolley int [not NULL]weaponQTY int[not NULL]);")

    def create_table_engines(self):
        print("we are in create_table_engine")
        self.cursor.execute("create table Engine(engine text NOT NULL PRIMARY KEY,EnginePower int [not NULL], "
                            + "EngineType int [not NULL]);")

        self.dbConnection.commit()

    def createship(self):

        for line in DataDump.DataDump.namelist:
            line = line.rstrip()
            self.targetlist.append(line)
            self.SqlQuery = '''INSERT INTO Ships(ship, weapon, hull, engine) 
                            values({s}, {w}, {h}, {e});'''.format(s=self.sqlParamShipName, w=self.sqlParamWeapon,
                            h=self.sqlParamHull, e=self.sqlParamEngine)
            print(self.SqlQuery)
        print("get lucky with fill up our database let the magic begin.")
        self.cursor.execute(self.SqlQuery)
        self.cursor.execute()
        pass
