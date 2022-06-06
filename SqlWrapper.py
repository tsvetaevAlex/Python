import sqlite3
from sqlite3 import Error
import DataDump
from random import randrange


class SqlWrapper:

    def __init__(self, test_db_name):
        self.datadump = DataDump.DataDump()
        self.names = self.datadump.Shipnames
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
                            + "NULL], engine text[not NULL]);")


    def create_table_weapons(self):
        print("we are create_table_weapon")
        SqlQuery = ("""create  table Weapons(weapon text NOT NULL Primary KEY, int[notNULL] reload_speed"
                            "int[notNULL] rotation_speed int[not NULL] diameter int [not NULL], "
                            "powerVolley int [not NULL]weaponQTY int[not NULL]);""")
        self.cursor.execute(SqlQuery)
        self.dbConnection.commit()

    def insert_weapon_details(self):
        for weapon in self.datadump.Shipweapons:
            reload_speed = randrange(1, 20)
            rotation_speed = randrange(1, 20)
            powerVolley = randrange(1, 20)
            weaponQTY = randrange(1, 20)
            self.cursor.execute("""insert into Weapons (weapon, reload_speed, rotation_speed, powerVolley, weaponQTY) 
                                values({weapon}, {load}, {rota}, {pvoley}, {qty}))""".format(weapon=weapon, load=reload_speed,
                                rota=rotation_speed, pvoley=powerVolley, qty=weaponQTY))

    def create_table_engines(self):
        print("we are create_table_engine")
        SqlQuery = ("""create  table engines(engine text NOT NULL Primary KEY, int[notNULL] power int[notNULL] 
                        EngineType int[not NULL]);""")
        self.cursor.execute(SqlQuery)
        self.dbConnection.commit()

    def insert_engine_details(self):
        for engine in self.datadump.Shipengines:
            power = randrange(1, 20)
            EngineType = randrange(1, 20)
            self.cursor.execute("""insert into engines (engine, power, EngineType) 
                                values({engine}, {power}, {EngineType}))""".format(engine=engine,
                                                                                   power=power,
                                                                                   EngineType=EngineType))
        self.dbConnection.commit()

    def create_table_hulls(self):
        print("we are in create_table_hulls")
        SqlQuery = ("""create table hulls(hull text NOT NULL PRIMARY KEY,armor int [not NULL], "
                            "armorType int [not NULL], capacity int [not NULL])""")
        self.cursor.execute(SqlQuery)
        self.dbConnection.commit()

    def insert_hull_details(self):
        for hull in self.datadump.Shiphulls:
            armor = randrange(1, 20)
            armorType = randrange(1, 20)
            capacity = randrange(1, 20)
            self.cursor.execute("""insert into Hull (hull, armor, armorType, capacity) 
                            values({hull}, {armor}, {armorType}, {capacity}))""".format(hull=hull, armor=armor,
                            armorType=armorType, capacity=capacity))

    def BattleShips_CreateARmada(self):

        for line in self.names:
            shipname = line.rstrip()
            sqlParamHull = self.datadump.get_hull()
            sqlParamWeapon = self.datadump.get_weapon()
            sqlParamEngine = self.datadump.get_engine()
            SqlQuery = '''INSERT INTO Ships(ship, weapon, hull, engine) 
                            values({shipname}, {w}, {h}, {e});'''.format(shipname=shipname, w=sqlParamWeapon,
                            h=sqlParamHull, e=sqlParamEngine)
            print(SqlQuery)
            self.cursor.execute(SqlQuery)
            self.dbConnection.commit()
        print("get lucky with fill up our database let the magic begin.")
