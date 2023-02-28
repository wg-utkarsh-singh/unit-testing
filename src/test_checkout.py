from pytest import fixture
from checkout import Checkout


@fixture
def checkout():
    checkout = Checkout()
    return checkout

def test_can_add_item_price(checkout):
    checkout.add_item_price("bread", 20)

def test_can_add_item(checkout):
    checkout.add_item_price("milk", 30)
    checkout.add_item("milk")

def test_can_calc_total(checkout):
    checkout.add_item_price("bread", 20)
    checkout.add_item_price("milk", 30)
    checkout.add_item("bread")
    checkout.add_item("milk")
    assert checkout.calc_total() == 50


def test_can_add_discount(checkout):
    checkout.add_discount("bread", 2, 30)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount("bread", 2, 30)
    checkout.add_item("bread")
    checkout.add_item("bread")
    checkout.add_item("bread")
    checkout.add_item("bread")
    assert checkout.calc_total() == 60
