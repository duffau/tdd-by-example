import xunit as xu

test = xu.WasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)
