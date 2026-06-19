import random

file = open("./pet.txt", mode="w")

file_content = file.read()
file_content_list = file_content.split("\n")  # create array of pet

file.close()

print(random.choice(file_content_list))
