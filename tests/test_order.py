from typing import Any

import pytest

from src.order import Order


def test_order_add_product(smartphone_1: Any) -> None:
    order = Order()
    order.add_product(smartphone_1, 1)
    assert order.name == "Iphone 15"
    assert order.quantity == 1
    assert order.total_sum == 210000.0


def test_category_add_product_error(first_category: Any) -> None:
    with pytest.raises(TypeError):
        Order().add_product(first_category, 1)
