import traceback

from xunit import TestCase, WasRun, TestResult, TestSuite


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert test.log == "setUp testMethod tearDown "

    def testTemplateBrokenMethod(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert test.log == "setUp testBrokenMethod tearDown "

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert "1 run, 1 failed" == self.result.summary()
    
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()

    def testSuiteFromTestCase(self):
        suite = TestSuite(WasRun)
        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


suite = TestSuite(TestCaseTest)
result = TestResult()
suite.run(result)
print(result.summary())