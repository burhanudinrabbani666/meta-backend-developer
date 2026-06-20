# Logorihtmic time
def find_number(targert: int):
    iterations = 0
    x = range(100)
    left = 0
    right = len(x)

    while left <= right:
        iterations += 1
        middle = (left + right) // 2  # This is floor divide
        is_number = x[middle]

        print(left, right)

        if targert == is_number:
            print("Iterations", iterations)
            return middle
        elif targert < is_number:
            right = middle - 1
        else:
            left = middle + 1

    return -1


print(find_number(23))
