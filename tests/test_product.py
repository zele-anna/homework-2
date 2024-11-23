from typing import Any

from src.product import Product


def test_product(first_product: Any) -> None:
    assert first_product.name == "Xiaomi Redmi Note 11"
    assert first_product.description == "1024GB, Синий"
    assert first_product.price == 31000.0
    assert first_product.quantity == 14


def test_second_product(second_product: Any) -> None:
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_new_product() -> None:
    product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter(capsys: Any, first_product: Any) -> None:
    first_product.price = 800
    assert first_product.price == 800
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    first_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(first_product: Any) -> None:
    assert str(first_product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product_add(first_product: Any, second_product: Any) -> None:
    assert first_product + second_product == 2114000.00
