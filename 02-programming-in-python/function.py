def sum(x: int, y: int) -> float:
    return x + y


def calculateTax(bill: float, tax_rate: float) -> float:
    return round((bill * tax_rate) / 100.00, 2)


# Global scope
my_global: int = 10


def fn1():
    local_v = 10
    print("Access to global", my_global)

    def fn2():
        print("Access to enclosed", local_v)

    fn2()


fn1()
