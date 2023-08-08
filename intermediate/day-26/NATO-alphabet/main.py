import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# {new_key:new_value for (index, row) in df.iterrows()}
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

is_input_invalid = True

while is_input_invalid:
    try:
        word = input("Enter a word: ").upper()
        result = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_input_invalid = False
        print(result)

