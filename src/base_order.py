from abc import ABC, abstractmethod
from typing import Any


class BaseOrder(ABC):

    @abstractmethod
    def add_product(self, *args: Any, **kwargs: Any) -> None:
        pass
