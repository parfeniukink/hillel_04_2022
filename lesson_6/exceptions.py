data = ValueError("Hello from Hillel")

try:
    raise data
except Exception as error:
    print(f"error was raised.\n message: {error}")
