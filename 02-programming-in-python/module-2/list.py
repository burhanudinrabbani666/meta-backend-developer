from typing import Any

list1: list[int] = [1, 2, 3, 4, 5]
list2: list[str] = ["A", "B", "C"]
list3: list[Any] = ["Hello", 123, True]
list4: list[Any] = ["Hello", 123, True, [1, 2, 3, 4]]

print(list1[2])
print(list4[-1])

# List method
list1.insert(len(list1), 7)
list1.append(7)
list1.extend([6, 7, 8, 9, 10])

print(list1)

list1.pop(-1)
print(list1)

# del list1
# print(list1) # Error

for i in list1:
    print(f"Value: {i}")
