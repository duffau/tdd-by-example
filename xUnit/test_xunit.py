from xunit import TestCase, WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        assert self.test.log == "setUp "


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
