class DiscountEngine:
    def __init__(self, product: Product):
        ...


class Product:
    def __init__(self, name: str, price: int):
        self.name: str = name
        self.price: int = price


# apple = Prodcut(..)
# apple.price = ...


john = User(name="John", age=12)
john.is_adult
