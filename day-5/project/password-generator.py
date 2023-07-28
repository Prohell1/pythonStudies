# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nrLetters = int(input("How many letters would you like in your password?\n"))
nrSymbols = int(input(f"How many symbols would you like?\n"))
nrNumbers = int(input(f"How many numbers would you like?\n"))

randomLetters = random.choices(letters, k=nrLetters)
randomNumbers = random.choices(numbers, k=nrNumbers)
randomSymbols = random.choices(symbols, k=nrSymbols)

characters = []
for letter in randomLetters:
    characters.append(letter)
for number in randomNumbers:
    characters.append(number)
for symbol in randomSymbols:
    characters.append(symbol)

random.shuffle(characters)
password = "".join(characters)

print(f"Your password is {password}")
