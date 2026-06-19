# IndexError
items = [1, 2, 3, 4, 5]

try:
    item = items[6]
    print(item)
except IndexError as e:
    print("Item does not exist in the list,", e)


# ZeroDevisionError
def devide_by(a: float, b: float) -> float:
    return a / b


try:
    ans = devide_by(40, 0)
    print(ans)
except ZeroDivisionError as e:
    print("Cannot devide with 0,", e)


# FileNotFoundError

try:
    with open("file_does_not_exist.txt", "r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found,", e)
