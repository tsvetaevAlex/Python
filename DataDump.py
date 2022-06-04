import configparser
from distutils.command.config import config
from random import random, randrange
import TestEnvironment
from TestEnvironment import
def getweapon():
    return randrange(1, 20, 1)


def gethull():
    return randrange(1, 5, 1)


class DataDump:
    def __init__(self):

        self.namelist = []
        self.enginelist = []
        self.hulllist = []
        self.weaponlist = []

        self.rand = random()
        self.environment = TestEnvironment.
        self.config = configparser.ConfigParser()
        self.config.read("settings.ini")
        self.config = configparser.ConfigParser()
        self.shipNamesLis_filename = config["EQUIPMENT"]["ShipnameListFile"]
        self.shipNamesLis = self.environment.getlist(self, self.shipNamesLis_filename, self.namelist)
        self.enginesListFile = config["EQUIPMENT"]["EngineListFile"]
        self.enginesList = self.environment.getlist(self, self.enginesListFile, self.enginelist)
        self.weaponListFile = config["EQUIPMENT"]["weaponListFile"]
        self.weaponList =  self.environment.getlist(self, self.weaponListFile, self.weaponlist)
        self.hullListFile = config["EQUIPMENT"]["hullListFile"]
        self.hullList =  self.environment.getlist(self, self.hullListFile, self.hulllist)

    @staticmethod
    def get_weapon():
        return randrange(1, 20, 1)

    @staticmethod
    def get_engine():
        return randrange(1, 6, 1)

    def get_shipname(self):
        return random.choice(self.environment.namelist)

    def set_equipment_list_filename(self, enginenane_listfilename):
        self.enginesListFile = enginenane_listfilename
        # random.choice(city_list)
        with open(self.enginesListFile) as file:
            for line in file:
                engine = line.rstrip()
                self.enginesList.append(engine)
                print(engine)

