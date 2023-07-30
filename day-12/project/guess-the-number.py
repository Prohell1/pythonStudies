from art import logo
import random


def generate_secret_number():
    return random.randint(1, 100)


def choose_difficulty():
    input_is_invalid = True
    while input_is_invalid:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5


def check_guess(user_guess, number_to_guess):
    global chances
    if user_guess > number_to_guess:
        print("Too high.\nGuess again.")
        chances -= 1
    elif user_guess < number_to_guess:
        print("Too low.\nGuess again.")
        chances -= 1
    else:
        print(f"You got it! The answer was {secret}")
        exit()


def ask_for_input():
    input_is_invalid = True
    while input_is_invalid:
        guessed_num = input("Make a guess: ")
        if guessed_num.isnumeric():
            guessed_num = int(guessed_num)
            if 0 < guessed_num <= 100:
                return guessed_num


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
secret = generate_secret_number()
chances = choose_difficulty()
while chances > 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    guess = ask_for_input()
    check_guess(guess, secret)
print("You've run out of guesses, you lose.")


