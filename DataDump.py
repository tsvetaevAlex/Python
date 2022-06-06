import random
import configparser
import TestEnvironment
import main


class DataDump:
    def __init__(self):
        self.config = configparser
        self.config_filename = main.configuration_filename

        self.Shipnames = []
        self.Shipengines = []
        self.Shipweapons = []
        self.Shiphulls = []
        self.rand = random.random()

        self.environment = TestEnvironment.TestEnvironment()
        self.config = configparser.ConfigParser()
        self.config.read(self.environment.congig_filename)
        self.config = configparser.ConfigParser()
        self.shipNamesLis_filename = self.config["EQUIPMENT"]["ShipnameListFile"]
        self.enginesList_filename = self.config["EQUIPMENT"]["EngineListFile"]
        self.weaponList_filename = self.config["EQUIPMENT"]["weaponListFile"]
        self.hullList_filename = self.config["EQUIPMENT"]["hullListFile"]
        self.Shipnames = self.environment.getList_fromfile(self.shipNamesLis_filename)
        self.Shipengines = self.environment.getList_fromfile(self.enginesList_filename)
        self.Shipweapons = self.environment.getList_fromfile(self.weaponList_filename)
        self.Shiphulls = self.environment.getList_fromfile(self.hullList_filename)

    def get_shipname(self):
        return random.choice(self.Shipnames)

    def get_weapon(self):
        return random.choice(self.Shipweapons)

    def get_engine(self):
        return random.choice(self.Shipengines)

    def get_hull(self):
        return random.choice(self.Shiphulls)
