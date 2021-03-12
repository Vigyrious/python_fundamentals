word = input()
coffee = 0
while not word == "END":
    if word == "dog" or word == "DOG":
        if word == "dog":
            coffee += 1
        else:
            coffee += 2
    elif word == "cat" or word == "CAT":
        if word == "cat":
            coffee += 1
        else:
            coffee +=2
    elif word == "coding" or word == "CODING":
        if word == "coding":
            coffee += 1
        else:
            coffee += 2
    elif word == "movie" or word == "MOVIE":
        if word == "movie":
            coffee += 1
        else:
            coffee += 2
    word = input()
if (coffee > 5):
    print("You need extra sleep")
else:
    print(coffee)