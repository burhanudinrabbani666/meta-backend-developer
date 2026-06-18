# file = open("hello.txt", mode="r")
# data = file.read()
# print(data)
# file.close()

with open("hello.txt", mode="r") as file:
    print(file.read())
