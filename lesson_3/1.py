# List comprehension


def foo():
    data: list[int] = [i for i in range(10)]
    for i in data:
        yield i


# data = create_list(60_000_000)
for i in foo():
    print(i)
# print(data)

# for i in data:
#     print(i)
