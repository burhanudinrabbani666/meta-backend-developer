my_list: list[int] = [1, 2, 3]


def add_to_list(lst: list[int], item: int):
    new_list = lst.copy()  # Create copy of list
    new_list.append(item)
    return new_list


new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)
