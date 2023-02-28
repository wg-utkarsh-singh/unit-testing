class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass")

    def test1(self):
        print("Executing test1.")
        assert True

    def test2(self):
        print("Executing test2.")
        assert True

    def setup_method(self, method):
        if method == self.test1:
            print("Setting up test1.")
        elif method == self.test2:
            print("Setting up test2.")
        else:
            print("Setting up unknow test.")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1.")
        elif method == self.test2:
            print("\nTearing down test2.")
        else:
            print("\nTearing down unknow test.")
