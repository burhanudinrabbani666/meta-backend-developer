import time

start_time = time.time()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
# outer loop
for x in range(1000):
    # inner loop
    for y in range(10000):
        print(0, end=" ")


print(round((time.time() - start_time), 2))
