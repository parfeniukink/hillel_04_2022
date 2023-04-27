from dataclasses import dataclass
from enum import Enum
from time import sleep


class DishSize(Enum):
    S = "S"
    M = "M"
    L = "L"


@dataclass
class Dish:
    name: str
    size: DishSize
    ingredients: list[str]

    def __str__(self) -> str:
        return self.name


class Kitchen:
    """This class includes methods for cooking and heating dishes."""

    @staticmethod
    def heat(dish: Dish) -> None:
        """IO-bound task."""

        print(f"⏲️ Started heating {dish}")
        sleep(3)
        print(f"✅ The {dish} is warm")

    @staticmethod
    def cook(dish: Dish) -> None:
        """CPU-bound task."""

        print(f"\n⏲️ Started cook the {dish}")
        _ = [i for i in range(180_000_000)]
        print(f"✅ The {dish} is ready")
