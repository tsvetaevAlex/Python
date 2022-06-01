import TestEnvironment


class BattleShip:
    def __init__(self, name, weapon, hull, engine):
        self.environment = TestEnvironment.TestEnvironment("BattleShips_exam.db")
        self.environment.prepare()
        self.shipname = name
        self.shipweapon = weapon
        self.shiphull = hull
        self.shipengine = engine
        print("here we go.")


#ToDo it will be test class