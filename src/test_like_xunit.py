def test1():
    print("Executing test1.")
    assert True


def test2():
    print("Executing test2.")
    assert True


def setup_module(module):
    print("Setup module.")


def teardown_module(module):
    print("Teardown Module.")


def setup_function(func):
    if func == test1:
        print("Setting up test1.")
    elif func == test2:
        print("Setting up test2.")
    else:
        print("Setting up unknow test.")


def teardown_function(func):
    if func == test1:
        print("\nTearing down test1.")
    elif func == test2:
        print("\nTearing down test2.")
    else:
        print("\nTearing down unknow test.")
