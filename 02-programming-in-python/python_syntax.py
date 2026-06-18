from typing import Any

x = 1 + 2
name = "Bani"


def say_hello(name: str) -> Any:
    print(name)  # <--This is correct indent
    return


if name == "Bani":
    say_hello(name)
else:
    print("Wrong name")
