import asyncio


class Client:
    def __init__(self, ip: str):
        self._ip = ip

    def _close(self):
        print(f"Closing connection with {self._ip}")

    # async def __enter__(self):
    #     return self

    # async def __exit__(self, *args, **kwargs):
    #     return self._close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        return self._close()

    def print(self, msg: str):
        print(f"Printing... {msg}")




# def main():
#     with Client(ip="10.199.120.2") as client:
#         client.print("First one")
#     with Client(ip="192.168.120.3") as client:
#         client.print("Second one")
# main()


async def async_main():
    async with Client(ip="10.199.120.2") as client:
        client.print("First one")

    async with Client(ip="192.168.120.3") as client:
        client.print("Second one")


asyncio.run(async_main())


from dataclasses import dataclass
from random import randint

UserWithoutName = 

class User:
    def __init__(
            self, payload
    ) -> None:
        self.name = payload.name
        self.surname = payload.surname
        self.age = payload.age

    def create_without_name():
        pass

    def create_without_surname():
        pass

    def create_no_age_no_surname():
        pass


username = input()
surname = input()
