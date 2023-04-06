def foo():
    for i in range(10):
        yield f"foo {i}"


def bar():
    for i in range(10):
        print(f"I am from bar {i}")
        yield from foo()


for i in bar():
    print(i)
