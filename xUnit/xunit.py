class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = 1
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "