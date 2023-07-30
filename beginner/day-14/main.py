from art import logo, vs
from game_data import data
import random
from os import system


def compare(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")


def get_user_input():
    input_is_invalid = True
    while input_is_invalid:
        player_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if player_guess == 'A' or player_guess == 'B':
            return player_guess


def check_guess(comparable_a, comparable_b, user_guess):
    if comparable_a["follower_count"] > comparable_b["follower_count"]:
        winner = "A"
    else:
        winner = "B"
    if user_guess == winner:
        return True
    else:
        return False


def play_game():
    good_guesses = 0
    game_goes_on = True
    while game_goes_on:
        system('cls')
        print(logo)
        a, b = random.choices(population=data, k=2)
        while a == b:
            a, b = random.choices(population=data, k=2)
        compare(a, b)
        guess = get_user_input()
        guess_was_right = check_guess(a, b, guess)
        if guess_was_right:
            good_guesses += 1
            print(f"You're right! Current score: {good_guesses}.")
        else:
            game_goes_on = False
            print(f"Sorry, that was wrong. Final score: {good_guesses}")
            input("Press enter to exit")











play_game()