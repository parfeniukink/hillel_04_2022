from threading import Thread
from time import perf_counter, sleep


def loop(name: str):
    N = 100_000_000
    for _ in range(N):
        pass
    print(f"{name} is finished")


start = perf_counter()
loop("Root1")
loop("Root2")
loop("Root3")

# thread1 = Thread(target=loop, args=("T1",))
# thread2 = Thread(target=loop, args=("T2",))
# thread3 = Thread(target=loop, args=("T3",))

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

exec_time = perf_counter() - start

print(f"Execution time: {exec_time}")
