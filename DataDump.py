import configparser
from utils import get_equipmentlist_fromfile

class DataDump:
    def __init__(self):

        def config("settings.ini")
        self.config = configparser.ConfigParser()  # создаём объекта парсера
        self.shipNamesLis_filename = config["EQUIPMENT"]["ShipnameListFile"]
        self.shipNamesLis = []
        self.enginesListFile = config["EQUIPMENT"]["EngineListFile"]
        self.enginesList = []
        self.weaponListFile = config["EQUIPMENT"]["weaponListFile"]
        self.weaponList = []
        self.hullListFile = config["EQUIPMENT"]["hullListFile"]
        self.hullList = []

        self.shipNamesLis = utils.get_equipmentlist_fromfile(self.shipNamesLis_filename)
        self.enginesList = get_equipmentlist_fromfile(self.enginesListFile)
        self.weaponList = get_equipmentlist_fromfile(self.weaponListFile)
        self.hullList = get_equipmentlist_fromfile(self.hullListFile)

    def set_equipmentlist_filename(self, enginenaMes_listfilename):
        self.enginesListFile = enginenaMes_listfilename
        # random.choice(city_list)
        with open(self.enginesListFile) as file:
            for line in file:
                engine = line.rstrip()
                self.shipNamesLis.append(engine)
                print(engine)
