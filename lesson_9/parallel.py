from multiprocessing import Process
from time import perf_counter

from kitchen import Dish, DishSize, Kitchen


def main():
    pizza = Dish(
        name="Peperonny",
        size=DishSize.M,
        ingredients=["tomato", "cheese", "chicken"],
    )
    salad = Dish(
        name="Ceasar",
        size=DishSize.L,
        ingredients=["eggs", "cheese", "chicken"],
    )

    dishes: list[Dish] = [pizza, salad]
    threads: list[Process] = [
        Process(
            target=Kitchen.cook,
            args=[dish],
        )
        for dish in dishes
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"⛳Cooking time: {perf_counter() - start}")
