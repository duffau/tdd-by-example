class TestCase:
    def __init__(self, name):
        self.name = name

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = None
    
    def testMethod(self):
        self.wasRun = 1

    def run(self):
        method = getattr(self, self.name)
        method()