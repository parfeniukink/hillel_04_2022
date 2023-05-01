from time import sleep
import asyncio
from typing import Coroutine


async def foo():
    print("foo")
    await asyncio.sleep(3)
    print("Finishing foo")
    return "Result"


async def bar(value: str):
    print("bar")
    sleep(1)
    print(f"Result from foo: {value}")


async def main():
    tasks = [foo(), bar("Another")]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
    # main()
