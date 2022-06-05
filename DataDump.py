import random
import configparser
import TestEnvironment


class DataDump:
    def __init__(self):

        self.config = configparser
        self.namelist = []
        self.weaponlist = []
        self.enginelist = []
        self.hulllist = []
        self.rand = random.random()

        self.environment = TestEnvironment.TestEnvironment()
        self.config = configparser.ConfigParser()
        self.config.read(self.environment.congig_filename)
        self.config = configparser.ConfigParser()
        self.shipNamesLis_filename = self.config["EQUIPMENT"]["ShipnameListFile"]
        self.shipNamesLis = self.environment.getlist(self, self.shipNamesLis_filename, self.namelist)
        self.enginesListFile = self.config["EQUIPMENT"]["EngineListFile"]
        self.enginesList = self.environment.getlist(self, self.enginesListFile, self.enginelist)
        self.weaponListFile = self.config["EQUIPMENT"]["weaponListFile"]
        self.weaponList = self.environment.getlist(self, self.weaponListFile, self.weaponlist)
        self.hullListFile = self.config["EQUIPMENT"]["hullListFile"]
        self.hullList = self.environment.getlist(self, self.hullListFile, self.hulllist)

    @staticmethod
    def get_shipname(self):
        return random.choice(self.namelist)

    @staticmethod
    def get_weapon(self):
        return random.choice(self.weaponlist)

    @staticmethod
    def get_engine(self):
        return random.choice(self.enginelist)

    @staticmethod
    def get_hull(self):
        return random.choice(self.hulllist)
