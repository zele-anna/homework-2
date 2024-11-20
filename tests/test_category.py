from typing import Any


def test_category(first_category: Any, second_category: Any) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации."
    assert len(first_category.products_in_list) == 2
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Комфорт и эстетика."
    assert len(second_category.products_in_list) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_products_property(first_category: Any) -> None:
    assert first_category.products == (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_add_product(second_category: Any, first_product: Any) -> None:
    assert len(second_category.products_in_list) == 3
    second_category.add_product(first_product)
    assert len(second_category.products_in_list) == 4


def test_category_str(second_category: Any) -> None:
    assert str(second_category) == "Телевизоры, количество продуктов: 24 шт."
