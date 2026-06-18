num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

count = 0
for idx, num in enumerate(num_list):
    if num == 36:
        print(f"number 36 found at position: {idx}")
        break
    elif num >= 45:
        print(f"over 45")
    else:
        print(f"under 45")

    count += 1

print(count)
