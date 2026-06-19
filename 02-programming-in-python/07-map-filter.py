menu = ["expresso", "mocha", "latte", "cappucino", "cortado", "americano"]


def find_coffe(coffe: str):
    if coffe[0] == "c":
        return coffe


map_coffe = map(find_coffe, menu)
for x in map_coffe:
    print(x)

filter_coffe = filter(find_coffe, menu)
for x in filter_coffe:
    print(x)
