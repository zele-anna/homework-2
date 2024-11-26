from src.base_order import BaseOrder
from src.product import Product


class Order(BaseOrder):
    name: str
    quantity: int
    total_sum: float

    def __init__(self) -> None:
        self.name = ""
        self.quantity = 0
        self.total_sum = 0.0

    def add_product(self, product: Product, quantity: int) -> None:
        if isinstance(product, Product):
            self.name = product.name
            self.quantity = quantity
            self.total_sum = quantity * product.price
        else:
            raise TypeError
