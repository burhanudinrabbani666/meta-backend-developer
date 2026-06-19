favorites = ["ok computer", "loveless", "solvaki", "kid a"]

for idx, album in enumerate(favorites):
    print(f"{idx}. {album}")

count = 0
while count < len(favorites):
    print(f"My favorite album: {favorites[count]}")
    count += 1
