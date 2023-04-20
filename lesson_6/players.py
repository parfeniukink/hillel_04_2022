import random


def f(x):
    return x**2


class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name: str) -> "Player":
        return cls(name=name, age=random.randint(1, 18))

    @classmethod
    def create_adult(cls, name: str, age: int) -> "Player":
        return cls(name=name, age=random.randint(18, 100))


# john = Player()
# Player.create_adult(name="John", age=12)


class Team:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, players: list | None = None):
        if Team._initialized is True:
            return

        print(f"Initializing {self=}")
        self._team: list = players if players else []

        Team._initialized = True

    @staticmethod
    def divider():
        print("***********")

    def repr(self):
        self.divider()
        for player in self._team:
            print(f"Name: {player.name}, age: {player.age}")

    @classmethod
    def repr_players(cls, players: list[Player]):
        cls.divider()
        for player in players:
            print(f"Name: {player.name}, age: {player.age}")

    def add(self, player: Player) -> None:
        self._team.append(player)


john = Player(name="John", age=20)
marry = Player(name="Marry", age=30)
mark = Player.create_adult(name="Mar")

players: list[Player] = [john, marry, mark]

print("Creating dinamo")
dinamo = Team(players)
print(f"{id(dinamo)=}")
print(dinamo._team)
print(f"{Team._instance=}\n\n")

print("Creating another team")
another = Team()
print(f"{id(another)=}")
print(f"{Team._instance=}")

print("\n\n")
print(dinamo._team)

# john.repr_players(players)
# Player.repr_players(john, players)
# repr_players(players)
# dinamo.repr()

# another_team: list[Player] = [john, mark]
# Team.repr_players(another_team)
