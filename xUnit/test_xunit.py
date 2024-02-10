import traceback

from xunit import TestCase, WasRun, TestResult


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
try:
    TestCaseTest("testFailedResult").run()
except Exception as e:
    traceback.print_exc()

TestCaseTest("testFailedResultFormatting").run()
