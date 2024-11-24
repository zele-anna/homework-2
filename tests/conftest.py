from typing import Any

import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def first_product() -> Any:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def second_product() -> Any:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def first_category(first_product: Any, second_product: Any) -> Any:
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации.", [first_product, second_product])


@pytest.fixture
def second_category(first_product: Any, second_product: Any) -> Any:
    return Category(
        "Телевизоры",
        "Комфорт и эстетика.",
        [first_product, second_product, Product("Пылесос Xiaomi", "Dreame v12", 20999.99, 2)],
    )


@pytest.fixture
def product_iterator(first_category: Any) -> Any:
    return ProductIterator(first_category)


@pytest.fixture
def smartphone_1() -> Any:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_2() -> Any:
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawn_grass_1() -> Any:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2() -> Any:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
