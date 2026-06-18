# Args


from typing import TypedDict, Unpack


def sum_of(*args: int) -> int:
    sum = 0
    for x in args:
        sum += x

    return sum


# print(sum_of(1, 2, 3, 4))


class bill_items(TypedDict):
    Cofee: float
    Cake: float
    Juice: float


def total_bill(**kwargs: Unpack[bill_items]):
    print(kwargs)
    total: float = 0
    for v in kwargs.values():
        total += v  # type: ignore

    return round(total, 2)  # type: ignore


print(total_bill(Cofee=2.09, Cake=4.55, Juice=2))
