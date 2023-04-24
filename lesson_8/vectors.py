# a = ((1, 2), (3, 4))
# b = ((1, 2), (3, 4))

# Vector = tuple[tuple[int, int]]


# def summarize(a: Vector, b: Vector) -> Vector:
#     return (
#         (a[0][0] + b[0][0], a[0][1] + b[0][1]),
#         (a[1][0] + b[1][0], a[1][1] + b[1][1]),
#     )

from dataclasses import dataclass


@dataclass
class Point:
    __slots__ = ("x", "y")

    x: int
    y: int

    # @staticmethod
    # def foo():
    #     pass

    def __add__(self, other: "Point") -> "Point":
        return Point(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        pass

    def __enter__():
        pass

    def __exit__():
        pass

    def __aenter__():
        pass

    def __aexit__():
        pass

    def __bool__():
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass


# next(Point())


@dataclass
class Vector:
    start: Point
    end: Point

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            start=self.start + other.start,
            end=self.end + other.end,
        )


a = Vector(start=Point(x=1, y=1), end=Point(x=3, y=2))
b = Vector(start=Point(x=5, y=0), end=Point(x=6, y=3))
# c = Point(x=3, y=2)

d = a + b


len(a)
