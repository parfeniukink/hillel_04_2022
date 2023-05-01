import asyncio
from random import randint


def get_random_countdown() -> int:
    return randint(1, 3)


def get_random_delay() -> int:
    return randint(2, 5)


async def start_countdown(number):
    print("Starting countdown...")
    for i in reversed(range(number)):
        print(f"{i}...")
        await asyncio.sleep(1)


async def start_delay(number: int) -> None:
    print(f"Waiting for {number} seconds")
    await asyncio.sleep(number)


async def launch_rocket(num):
    delay = get_random_delay()
    countdown = get_random_countdown()
    await start_delay(delay)
    await start_countdown(countdown)
    print(f"Rocket {num} is in the space")


async def main():
    tasks = [launch_rocket(num) for num in range(10_000)]
    await asyncio.gather(*tasks)


asyncio.run(main())
