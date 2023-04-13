from functools import wraps

# Connection: IP:PORT

# def disconnect(ip: str, port: int) -> None:
#     print(f"Closing connection: {ip}:{port}")


def connect(ip: str, port: int):
    def inner(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            """Wrapper"""
            print(f"Connecting to the printer: {ip}:{port}")
            function(*args, **kwargs)
            print(f"Closing connection: {ip}:{port}")

        return wrapper

    return inner


@connect(ip="192.168.1.10", port=5432)
def print_black_white(document: str):
    """Black white function"""
    print(f"Printing bw...\n{document}")


@connect(ip="192.168.1.10", port=5432)
def print_colorized(document: str):
    print(f"Printing c...\n{document}")


def main():
    text = "Hello Python"
    print_black_white(document=text)
    print(print_black_white.__doc__)
    # connection_info = dict(ip="192.168.1.10", port=5432)
    # connect(**connection_info)
    # disconnect(**connection_info)


if __name__ == "__main__":
    main()
