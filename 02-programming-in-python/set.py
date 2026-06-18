set_a: set[int] = {1, 2, 3, 4, 5, 6}
set_b: set[int] = {6, 7, 8, 9, 10, 11, 12}

print(set_a)

set_a.add(7)
set_a.remove(7)
set_a.discard(7)

print(set_a | set_b)
print(set_a.union(set_b))

print(set_a & set_b)
print(set_a - set_b)

print(set_a.symmetric_difference(set_b))  # not in same
print(set_a ^ set_b)  # not in same

# get set value
# set is not base on index
