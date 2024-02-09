class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        self.wasSetUp = 1

    def run(self):
        method = getattr(self, self.name)
        self.setUp()
        method()


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1
