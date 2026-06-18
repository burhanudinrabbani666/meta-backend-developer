# snake_case is convention in python code base
# typing in python is just for hint
# typing in python not for strict the value
first_name: str = "burhanudin"
last_name: str = "rabbani"
print(f"my name is {first_name} {last_name}.")

first_name = 24  # This is valid
print(first_name)

# Delete variable
del first_name
print(first_name)  # Error: name is not defined
