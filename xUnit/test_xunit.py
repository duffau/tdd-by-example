from xunit import TestCase, WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        self.test.run()
        assert self.test.log == "setUp testMethod "


TestCaseTest("testTemplateMethod").run()
