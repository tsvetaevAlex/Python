import configparser
from distutils.command.config import config
from random import random, randrange

#from TestEnvironment import namelist
import TestEnvironment

from utils import get_equipmentlist_fromfile


def getweapon():
    return randrange(1, 20, 1)


class DataDump:
    def __init__(self):
        selr.rand = random()
        self.environment = TestEnvironment
        self.config = configparser.ConfigParser()
        self.config.read("settings.ini")
        self.config = configparser.ConfigParser()  # создаём объекта парсера
        self.shipNamesLis_filename = config["EQUIPMENT"]["ShipnameListFile"]
        self.shipNamesLis = []
        self.enginesListFile = config["EQUIPMENT"]["EngineListFile"]
        self.enginesList = []
        self.weaponListFile = config["EQUIPMENT"]["weaponListFile"]
        self.weaponList = []
        self.hullListFile = config["EQUIPMENT"]["hullListFile"]
        self.hullList = []

        self.shipNamesLis = get_equipmentlist_fromfile(self.shipNamesLis_filename)
        self.enginesList = get_equipmentlist_fromfile(self.enginesListFile)
        self.weaponList = get_equipmentlist_fromfile(self.weaponListFile)
        self.hullList = get_equipmentlist_fromfile(self.hullListFile)

    def gethull(self):
        return randrange(1, 5, 1)

    def getweapon(self):
        return randrange(1, 20, 1)

    def getengine(self):
        return randrange(1, 6, 1)

    def geshipname(self):
        return random.choice(self.environment.namelist)

    def set_equipmentlist_filename(self, enginenane_listfilename):
        self.enginesListFile = enginenane_listfilename
        # random.choice(city_list)
        with open(self.enginesListFile) as file:
            for line in file:
                engine = line.rstrip()
                self.enginesList.append(engine)
                print(engine)

