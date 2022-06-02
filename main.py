from TestEnvironment import TestEnvironment


if __name__ == '__main__':
    environment = TestEnvironment("examBattleSHip.db")
    environment.get_ship_namelist("ListOfNames.txt")

    #environment.prepare()
    #environment.cleanUp()
