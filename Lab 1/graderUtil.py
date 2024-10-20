
class Grader:
    def __init__(self):
        self.basicTests = []
        self.hiddenTests = []

    def addBasicPart(self, name, testFunc):
        self.basicTests.append((name, testFunc))

    def addHiddenPart(self, name, testFunc):
        self.hiddenTests.append((name, testFunc))

    def requireIsEqual(self, expected, actual):
        assert expected == actual, f"Expected {expected}, but got {actual}"

    def grade(self):
        print("Running basic tests...")
        for name, test in self.basicTests:
            try:
                test()
                print(f"Basic test {name} passed!")
            except AssertionError as e:
                print(f"Basic test {name} failed: {e}")

        print("Running hidden tests...")
        for name, test in self.hiddenTests:
            try:
                test()
                print(f"Hidden test {name} passed!")
            except AssertionError as e:
                print(f"Hidden test {name} failed: {e}")
            except Exception as e:
                print(f"Hidden test {name} crashed: {e}")
