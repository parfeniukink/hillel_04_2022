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

    for dish in dishes:
        Kitchen.cook(dish)


if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"⛳Cooking time: {perf_counter() - start}")
