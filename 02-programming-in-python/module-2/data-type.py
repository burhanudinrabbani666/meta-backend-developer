from typing import Any

# NUMERIC
currency: float = 10.4
football_score: int = 5

# SEQUENCE
first_name: str = "Burhanudin"

students_list_str: list[str] = ["bani", "agus", "heri"]  # List of string
students_list_any = ["bani", 23, True]  # List of any data type

students_tuple = (1, "bani", 5, "A")  # tuple data types
print(students_tuple[1])

student_dict: dict[str, Any] = {"name": "burhanudin", "age": 23}
print(student_dict.get("name"))

# BOOLEAN
is_true: bool = True
is_false: bool = False

print(type(is_true))
