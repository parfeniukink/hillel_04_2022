def custom_range(n: int, start: int | None = None):
    counter = start or 0

    while n > counter:
        print(f"Yielding {counter}")
        yield counter
        print(f"Incrementing {counter}")
        counter += 1


gen = custom_range(5)

while True:
    try:
        data = next(gen)
        data = next(gen)
    except StopIteration:
        print("Finished")
        break
