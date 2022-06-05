from TestEnvironment import TestEnvironment


if __name__ == '__main__':
    environment = TestEnvironment()
    environment.setCongigFIleName("setting.ini")
    environment.prepare(self)
    print("HOORAY")
    environment.cleanup(self)
