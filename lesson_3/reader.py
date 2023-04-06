# def find_in_file(file_name: str, pattern: str) -> list[str]:
#     results = []
#     with open(file_name, "r") as file:
#         lines = file.readlines()
#         print(f"SIZE: {sys.getsizeof(lines)}")
#         for word in lines:
#             if pattern in word:
#                 yield word

#     return results


def find_in_file(file_name: str, pattern: str):
    with open(file_name, "r") as file:
        while True:
            line = file.readline().replace("\n", "")
            if not line:
                break
            if pattern in line:
                yield line


data = find_in_file(
    file_name="./lesson_3/rockyou.txt",
    pattern="john",
)


results = list(data)

print(len(results))
print(results[:10])
