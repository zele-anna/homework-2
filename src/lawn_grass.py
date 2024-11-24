from typing import Any

from src.product import Product


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> Any:
        if type(other) is LawnGrass:
            sum_price = self.quantity * self.price + other.quantity * other.price
            return sum_price
        else:
            raise TypeError
