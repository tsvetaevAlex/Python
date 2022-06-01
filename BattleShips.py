import  TestEnvironment


class BattleShip:
    def __init__(self, name, weapon, hull, engine):
        self.environment = TestEnvironment
        self.environment.prepare("BattleShips_exam.db")
            self.shipname = name
            self.shipweapon = weapon
            self.shiphull = hull
            self.shipengine = engine
            print("here we go.")
