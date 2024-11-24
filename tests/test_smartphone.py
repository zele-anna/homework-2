from typing import Any

import pytest


def test_smartphone_init(smartphone_1: Any) -> None:
    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.description == "512GB, Gray space"
    assert smartphone_1.price == 210000.0
    assert smartphone_1.quantity == 8
    assert smartphone_1.efficiency == 98.2
    assert smartphone_1.model == "15"
    assert smartphone_1.memory == 512
    assert smartphone_1.color == "Gray space"


def test_smartphone_add(smartphone_1: Any, smartphone_2: Any) -> None:
    assert smartphone_1 + smartphone_2 == 2114000.0


def test_smartphone_add_error(smartphone_1: Any) -> None:
    with pytest.raises(TypeError):
        float(smartphone_1 + 1)
