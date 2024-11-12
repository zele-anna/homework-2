import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def second_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def first_category(first_product, second_product):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации.", [first_product, second_product])


@pytest.fixture
def second_category(first_product, second_product):
    return Category(
        "Телевизоры",
        "Комфорт и эстетика.",
        [first_product, second_product, Product("Пылесос Xiaomi", "Dreame v12", "20999.99", 2)],
    )
