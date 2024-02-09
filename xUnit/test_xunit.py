from xunit import TestCase, WasRun


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
