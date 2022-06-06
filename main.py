import TestEnvironment

configuration_filename = "setting.ini"
exam_database = "ArmadaTest.db"
if __name__ == '__main__':
    environment = TestEnvironment.TestEnvironment()

environment.prepare()
print("HOORAY")
environment.cleanup()
