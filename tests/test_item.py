import pytest


from src.item import Item

@pytest.fixture
def item1():
    return Item("test", 10, 10)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 100


def test_apply_discount(item1):
    assert item1.apply_discount() == 8

def test_instantiate_from_csv():
   Item.instantiate_from_csv('./src/items.csv')

def test__str__(item1):
    assert str(item1) == "test"

def test_name(item1):
    assert item1.name == "test"


def test__repr__(item1):
    assert repr(item1) == "Имя: test, цена: 10"