from time import perf_counter, sleep

from kitchen import Dish, DishSize, Kitchen, DishState


# States
# def heat(dish: Dish):
#     temp_time = 0
#     while True:
#         if dish.state == DishState.NOT_STARTED:
#             dish.state = DishState.IN_PROGRESS
#             print(f"Dish {dish} started")
#         elif dish.state == DishState.IN_PROGRESS:
#             if dish.time_to_heat < temp_time:
#                 dish.state = DishState.DONE
#             else:
#                 temp_time += 1
#                 # yield
#                 sleep(1)
#         elif dish.state == DishState.DONE:
#             print("Dish is ready")
#             break


def main():
    pizza = Dish(
        name="Peperonny",
        size=DishSize.M,
        ingredients=["tomato", "cheese", "chicken"],
        time_to_heat=3,
    )
    salad = Dish(
        name="Ceasar",
        size=DishSize.L,
        ingredients=["eggs", "cheese", "chicken"],
        time_to_heat=5,
    )

    dishes: list[Dish] = [pizza, salad]

    for dish in dishes:
        Kitchen.heat(dish)


if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"⛳Cooking time: {perf_counter() - start}")
