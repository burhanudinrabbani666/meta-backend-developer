try:
    with open("sample/newFile.txt", mode="a") as file:
        file.writelines(
            [
                "\nThis is a new file created!",
                "\nThis a second line",
            ]
        )

except FileNotFoundError as e:
    print(e)
