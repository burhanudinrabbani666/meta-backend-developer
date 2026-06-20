class Employee:
    name: str
    last: str

    def __init__(self, name: str, last: str) -> None:
        self.name = name
        self.last = last


class Supervisor(Employee):
    password: str

    def __init__(self, name: str, last: str, password: str) -> None:
        super().__init__(name, last)
        self.password = password


class Chief(Employee):
    def leave_quest(self, days: float):
        return f"May i take a leave for {str(days)} days"


adrian = Supervisor(name="Adrina", last="A", password="apple")
emily = Chief(name="Emily", last="E")
june = Chief(name="June", last="J")

print(emily.leave_quest(3))
print(adrian.password)
print(june.name)
