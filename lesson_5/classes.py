from dataclasses import dataclass


class Adult:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name

        self._age_is_valid(age)
        self._age: int = age

    def _age_is_valid(self, value: int) -> None:
        if value < 18:
            raise Exception("Not adult")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        self._age_is_valid(value)
        print(f"New age is {value}")


john = Adult(name="John", age=89)
print(john.age)
john.age = 100


# class User:
#     def __init__(self, name: str, age: int) -> None:
#         self.name: str = name
#         self.age: int = age

#     @property
#     def adult(self) -> bool:
#         if self.age < 18:
#             return False
#         return True


# john = User(name="John", age=12)
# if john.adult:
#     ...


class Database:
    def __init__(self, host: str) -> None:
        self._last_id = 0
        self._host = host
        print(f"Connection to the SQLite: {host}")

    def __get__(self):
        pass

    def get(self, id_: int) -> dict:
        pass

    def delete(self, id_: int) -> None:
        pass

    def save(self, value: dict) -> dict:
        print(f"Saving to the database {self._host}...")
        self._last_id += 1
        value.update({"id": self._last_id})
        return value


@dataclass
class User:
    name: str
    age: int
    id: int | None = None


class UsersService:
    db = Database(host="localhost:5432")
    # def __init__(self) -> None:
    #     self._db: Database = Database(host="localhost:5432")

    def create(self, user: User) -> User:
        payload = {
            "name": user.name,
            "age": user.age,
        }
        new_payload = self.db.save(payload)
        return User(**new_payload)


john_not_created = User(name="John", age=20)
marry_not_created = User(name="Marry", age=20)

service = UsersService()

john = service.create(user=john_not_created)
marry = service.create(user=marry_not_created)

print(john)
print(marry)
