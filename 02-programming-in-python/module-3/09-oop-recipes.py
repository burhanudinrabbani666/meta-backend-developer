class Recipe:

    dish: str
    items: list[str]
    time: float

    def __init__(self, dish: str, items: list[str], time: float) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def content(self) -> str:
        return (
            f"The {self.dish} has {str(self.items)} and "
            f"takes {str(self.time)} min to proccess."
        )


pizza = Recipe("Pizza", ["Chesse", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["Penne", "Sauce"], 55)

# print(pizza.items)
# print(pasta.items)

# print(pizza.content())
# print(pasta.content())


class MyFirstClass:
    index: str = "Auhtor-Book"
    print("Who wrote this?")

    def hand_list(self, philosoper: str, book: str):
        print(self.index)
        print(f"{philosoper} wrote the book: {book}")


whodunni = MyFirstClass()
whodunni.hand_list(philosoper="Sun Tzu", book="The Art of War")
