class Payslips:

    name: str
    already_paid: bool
    amount: float

    def __init__(self, name: str, already_paid: bool, amount: float) -> None:
        self.name = name
        self.already_paid = already_paid
        self.amount = amount

    def pay(self):
        self.already_paid = True

    def status(self):
        if self.already_paid:
            return f"{self.name} is paid {str(self.amount)}"
        else:
            return f"{self.name} is not paid yet"


nathan = Payslips("nathan", False, 1000)
roger = Payslips("roger", False, 3000)


print(nathan.status())
print(roger.status())

nathan.pay()
print("After payment")
print(nathan.status())
print(roger.status())
