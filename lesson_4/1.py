# all / any
# all([...])

# reversed / reverse

# id -> RAM
# sum([1,23,4,5,6,7,8,9,])

# type / isinstance
# help
# int / str / ...
# print / input
# len
# del
# vars
# zip()

# from itertools import zip_longest

# users = {"john": 12, "marry": 32}


# user_names = ["john", "marry", "qwe"]
# user_surnames = ["Doe", "Coe"]
# user_ages = [12, 32]

# for name, surname, age in zip_longest(user_names, user_surnames, user_ages):
#     print(f"{name} {surname}, {age}")


# getattr

# data = john.get_name
# func.get_name
# data()

# john.get_name()
# func_get_name = getattr(john, "get_name")
# func_get_name()

# setattr / getattr / hasattr / delattr

from dataclasses import dataclass


class Validator:
    mandatory_fields = []

    def validate(self):
        for field in self.mandatory_fields:
            attr = getattr(self, field)
            if not attr:
                raise ValueError(f"Field {field} is mandatory")


@dataclass
class User(Validator):
    name: str
    age: int

    mandatory_fields = ["name", "age"]

    def greening(self):
        self.validate()
        print(f"Hi! I am {self.name}. I am {self.age}")


def validate(instance):
    for field in instance.mandatory_fields:
        attr = getattr(instance, field)
        if not attr:
            raise ValueError(f"Field {field} is mandatory")
    return instance


john = User(name="John", age=12)
marry = User(name="Marry", age=12)

elements = [john, marry]


def capitalize_name(user: User):
    setattr(user, "name", getattr(user, "name").capitalize())


for user in map(capitalize_name, elements):
    print(user)

john.greening()
getattr(john, "qwe")
