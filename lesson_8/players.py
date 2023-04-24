from enum import Enum
from typing import Callable


class Option(str, Enum):
    LIST = "list"
    ADD = "add"
    DELETE = "delete"


def players_add():
    pass


def players_list():
    pass


def players_delete(id_: int):
    pass


OPTION_CALLBACK_MAPPING: dict[str, Callable] = {
    Option.LIST: players_list,
    Option.DELETE: players_delete,
}


def _player_add_input() -> tuple:
    ...


def main():
    options = [str(option) for option in Option]
    user_choice = input(f"Select the option [{options}]: ")

    if user_choice not in options:
        raise ValueError("Not in optinos")

    callback = OPTION_CALLBACK_MAPPING[user_choice]
    input_data: tuple

    match user_choice:
        case Option.ADD:
            input_data = _player_add_input()
        case Option.LIST:
            input_data = _player_add_input()
        case Option.DELETE:
            input_data = _player_add_input()
        case _:
            raise ValueError("Not in optinos")

    callback(*input_data)


text = (
    "Sed volutpat ligula at accumsan vulputate. "
    "Sed congue lectus et vehicula ullamcorper. "
    "Donec est ipsum, sodales a consequat et, hendrerit ut enim. "
    "Phasellus vel erat a elit iaculis euismod. Ut eu congue dolor. "
)
