from TestEnvironment import TestEnvironment

if __name__ == '__main__':
    environment = TestEnvironment("ListOfNames.txt")

    environment.prepare()
    print("HOORAY")
    environment.cleanUp()
