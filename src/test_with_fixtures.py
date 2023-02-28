from pytest import fixture


@fixture(scope="module", autouse=True)
def setup_module():
    print("\nSetup module")


@fixture(scope="function", autouse=True)
def setup_function():
    print("\nSetup function")
    yield
    print("\nTrowback function")


def test1():
    print("Executing test1.")
    assert True


def test2():
    print("Executing test2.")
    assert True
