class TestSuite:
    def __init__(self, testCase):
        self.tests = []
        self._add_from(testCase)

    def _add_from(self, testCase):
        test_method_names = [
            method_name
            for method_name in dir(testCase)
            if method_name.startswith("test")
        ]
        for method_name in test_method_names:
            self._add(testCase(method_name))

    def _add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        finally:
            self.tearDown()
        return result


class TestResult:

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return f"{self.runCount} run, {self.errorCount} failed"


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        self.log += "testBrokenMethod "
        raise Exception

    def tearDown(self):
        self.log += "tearDown "
