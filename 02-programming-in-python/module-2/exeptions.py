def devide_by(a: float, b: float) -> float:
    return a / b


try:
    ans = devide_by(20, 0)
except ZeroDivisionError as e:
    print("Something went wrong!", e)
except Exception as e:
    print("Something went wrong!", e)
