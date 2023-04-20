# PayPal
# Stripe

from dataclasses import dataclass
import uuid
from abc import ABC, abstractmethod


@dataclass
class User:
    id_: int
    name: str
    surname: str
    age: int


@dataclass
class Product:
    id_: int
    name: str
    price: float

    def __repr__(self):
        return f"Product: {self.name}: {self.price}"


class PaymentSystem(ABC):
    @abstractmethod
    def authorize(self, user: User):
        """Authorize with external system."""

    @abstractmethod
    def checkout(self, product: Product):
        """Payment entrypoint."""

    @property
    @abstractmethod
    def status(self):
        """Represents the status of a checkout."""


class Stripe(PaymentSystem):
    def _get_token(self, user: User):
        return uuid.uuid3(uuid.NAMESPACE_DNS, str(user.id_))

    def _send_callback_api(self, token: str):
        print(f"Authirizing with Stripe: {token}")

    def authorize(self, user: User) -> bool:
        token = self._get_token(user)
        self._send_callback_api(token)
        return True

    def checkout(self, product: Product):
        self._status = True
        print(f"Checking out the {product=}")

    @property
    def status(self):
        if getattr(self, "_status", False):
            return "SUCCESS"
        return "FAILED"


class PayPal(PaymentSystem):
    MARKUP = 1.1

    def _get_token(self, user: User):
        return uuid.uuid5(uuid.NAMESPACE_DNS, str(user.id_))

    def _send_callback_api(self, token: str):
        print(f"Authirizing with PayPal: {token}")

    def authorize(self, user: User) -> bool:
        token = self._get_token(user)
        self._send_callback_api(token)
        return True

    def checkout(self, product: Product):
        product.price *= self.MARKUP
        print(f"Checking out the {product=}")

    @property
    def status(self):
        if getattr(self, "_status", False):
            return "SUCCESS"
        return "FAILED"


class Liqpay(PaymentSystem):
    MARKUP = 1.3

    def _get_token(self, user: User):
        return uuid.uuid5(uuid.NAMESPACE_DNS, str(user.id_))

    def _send_callback_api(self, token: str):
        print(f"Authirizing with Liqpay: {token}")

    def authorize(self, user: User) -> bool:
        token = self._get_token(user)
        self._send_callback_api(token)
        return True

    def checkout(self, product: Product):
        product.price *= self.MARKUP
        print(f"Checking out the {product=}")

    @property
    def status(self):
        if getattr(self, "_status", False):
            return "SUCCESS"
        return "FAILED"


class PaymentProcessor:
    def __init__(self, payment_system: PaymentSystem):
        self._payment_system = payment_system

    def checkout(self, user: User, product: Product):
        self._payment_system.authorize(user)
        self._payment_system.checkout(product)

    def get_status(self):
        return self._payment_system.status


def payment_system_dispatcher(decision: str) -> PaymentSystem:
    if decision == "stripe":
        return Stripe()
    if decision == "paypal":
        return PayPal()
    if decision == "liqpay":
        return Liqpay()

    raise Exception("Unknown payment system")


def main():
    john = User(id_=1, name="John", surname="Doe", age=20)
    apple = Product(id_=1, name="Apple", price=5)

    payment_system: PaymentSystem = payment_system_dispatcher("paypal")

    payment_processor = PaymentProcessor(payment_system)
    payment_processor.checkout(john, apple)
    status = payment_processor.get_status()

    print(status)


if __name__ == "__main__":
    main()
