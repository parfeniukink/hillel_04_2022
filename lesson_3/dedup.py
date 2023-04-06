# data = []


# def exist(payload: str) -> bool:
#     if payload not in data:
#         data.append(payload)
#         return False

#     print("Value already exists")
#     return True


def dedup_input():
    data = set()

    while payload := input("Enter the value: "):
        if payload not in data:
            data.add(payload)
            yield payload
        else:
            print("Value already exists")


def main():
    for payload in dedup_input():
        print(payload)


if __name__ == "__main__":
    main()
