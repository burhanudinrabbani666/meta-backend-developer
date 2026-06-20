from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def donate(self) -> float:
        pass


class Donation(Employee):
    def donate(self) -> float:
        a = input("How much you like to donate: ")
        return float(a)


amount: list[float] = []
jhon = Donation()
j = jhon.donate()
amount.append(j)

peter = Donation()
p = peter.donate()
amount.append(p)

print(amount)
