# Connection: IP:PORT

# def disconnect(ip: str, port: int) -> None:
#     print(f"Closing connection: {ip}:{port}")




class Connection:
    def __init__(self, ip: str, port: int) -> None:
        self.name = "HP"
        self._ip: str = ip
        self._port: int = port

    def __enter__(self):
        self.document = input("Enter the text to print: ")
        print(f"Connecting to the printer: {self._ip}:{self._port}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection: {self._ip}:{self._port}")

    def print_black_white(self):
        print(f"Printing bw using {self.name}...\n{self.document}")

    def print_colorized(self):
        print(f"Printing colorized using {self.name}...\n{self.document}")


def main():
    with Connection(ip="192.168.1.19", port=5432) as connection:
        connection.print_black_white()

    with Connection(ip="192.168.1.10", port=6453) as connection:
        connection.print_colorized()

    # connection_info = dict(ip="192.168.1.10", port=5432)
    # connect(**connection_info)
    # disconnect(**connection_info)


if __name__ == "__main__":
    main()
