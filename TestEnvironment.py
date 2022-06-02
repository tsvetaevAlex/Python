from SqlWrapper import SqlWrapper
import utils
import os

class TestEnvironment:

    def __init__(self):
        self.database_name = exam_database_name
        self.sql = SqlWrapper(exam_database_name)

        self.namelist = []
        self.enginelist = []
        self.hulllist = []
        self.weaponlist = []



    def prepare(self):
        utils.set_enginename_listfilename
        print("going to create a ", self.database_name, "data base")
        self.sql.create_database(self.database_name)
        self.sql.create_table_ships()
        self.sql.create_table_hull()
        self.sql.create_table_weapons()
        self.sql.create_table_engines()

    def getlits(self, filename):
        #random.choice(city_list)
        with open(filename) as file:
            for line in file:
                shipname = line.rstrip()
                self.namelist.append(shipname)
                print(shipname)

                #query = "insert into ship"
                #self.sql.process_query(self,query)


    def cleanup(self):
        print("CleanUp envitonment, delete outdated test database: ", self.database_name)
        print("\r\n")
        if os.path.isfile(self.database_name):
            os.remove(self.database_name)

        utils.set_enginenamelist_filename("EngineTypeList.txt")
        utils.set_shipameslist_filename("ListOfShipNames.txt")
        utils.set_weaponlist_filename("weaponList.txt")
        utils.set_hulllist_filename("")
