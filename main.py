import TestEnvironment


environment = TestEnvironment.TestEnvironment()

environment.prepare()
print("HOORAY")
environment.cleanup()
