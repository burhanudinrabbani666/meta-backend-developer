def sum(x: int, y: int) -> int:
    return x + y


def calculateTax(bill: float, tax_rate: float) -> float:
    return round((bill * tax_rate) / 100.00, 2)


print(sum(10, 13))
print("total tax:", calculateTax(175.00, 15))
