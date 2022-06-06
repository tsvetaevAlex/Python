import random
import Conf


class DataDump:
    def __init__(self, testEnvironment):
        self.environment = testEnvironment
        self.config_filename = Conf.configuration_filename

        self.Shipnames = []
        self.Shipengines = []
        self.Shipweapons = []
        self.Shiphulls = []
        self.rand = random.random()

        self.shipNamesLis_filename = Conf.BattleShipNames
        self.enginesList_filename = Conf.BattleShipEngines
        self.weaponList_filename = Conf.BattleShipWeapons
        self.hullList_filename = Conf.BattleShipHulls
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
