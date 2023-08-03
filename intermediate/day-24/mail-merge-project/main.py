# Getting the names from the file
with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()
    for index, name in enumerate(names):
        names[index] = name.strip()

# Getting the raw letter from the file
with open("./Input/Letters/starting_letter.txt") as data:
    letter = data.read()

# Writing a new letter for each name
for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as new_letter:
        new_letter.write(letter.replace("[name]", name))



