import asyncio
from time import perf_counter
from random import randint
from dataclasses import dataclass
import requests


@dataclass
class Pokemon:
    id: int
    name: str


BASE_URL = "https://pokeapi.co/api/v2/pokemon/{id}"


async def get_pokemon(id_: int) -> Pokemon:
    allowed_keys: set = Pokemon.__dataclass_fields__.keys()

    response = await asyncio.to_thread(
        requests.get,
        BASE_URL.format(id=id_),
    )
    content: dict = response.json()

    filtered_payload: dict = {
        key: value for key, value in content.items() if key in allowed_keys
    }

    pokemon = Pokemon(**filtered_payload)
    print(pokemon)
    return pokemon


async def main():
    tasks = [get_pokemon(id_=randint(10, 100)) for _ in range(50)]
    await asyncio.gather(*tasks)


def sync_main():
    for _ in range(50):
        pokemonchik = get_pokemon(id_=randint(10, 100))
        print(pokemonchik)


start = perf_counter()
asyncio.run(main())
# sync_main()
end = perf_counter()

print(f"⏲️ Total time: {end-start}")
