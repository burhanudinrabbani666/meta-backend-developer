from typing import Any

user: dict[str, Any] = {
    "first_name": "burhanudin",
    "last_name": "rabbani",
    "email": "bani@bani.io",
    "age": 23,
    "username": "bani1234",
}

print(type(user))
print(f"first name: {user['first_name']}")
print(f"last name: {user['last_name']}")
print(f"username: {user['username']}")
print(f"email: {user['email']}")

user["username"] = "bani son of dragon"

user.update({"is_handsome": True})
print(user)
