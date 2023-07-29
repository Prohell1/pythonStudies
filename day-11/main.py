from art import logo
from os import system
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    hand1 = random.choices(population=cards, k=2)
    hand2 = random.choices(population=cards, k=2)
    return hand1, hand2


def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score


def check_end_game(hand1, hand2):
    player_score = calculate_score(hand1)
    computer_score = calculate_score(hand2)
    condition = None

    if player_score == 21 and len(hand1) == 2:
        if computer_score == 21 and len(hand2) == 2:
            condition = "both_bj"
            return condition
        else:
            condition = "player_bj"
            return condition
    elif computer_score == 21 and len(hand2) == 2:
        condition = "computer_bj"
        return condition
    elif player_score > 21:
        condition = "player_bust"
        return condition
    return condition


def get_user_input():
    input_is_invalid = True
    while input_is_invalid:
        continuation = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continuation == "y" or continuation == "n":
            return continuation
        else:
            print("Please only enter 'y' or 'n'")


def draw_a_card(hand):
    hand.append(random.choice(cards))
    return hand


def computer_draws(hand):
    score = calculate_score(hand)
    while score < 17:
        hand = draw_a_card(hand)
        score = calculate_score(hand)
    return score, hand


def check_winner(p_hand, p_score, c_hand, condition):
    c_score = calculate_score(c_hand)
    if condition is None:
        c_score, c_hand = computer_draws(c_hand)
        if c_score > 21:
            condition = "computer_bust"
        elif c_score > p_score:
            condition = "lose"
        elif c_score == p_score:
            condition = "draw"
        else:
            condition = "win"
    print(f"Your final hand: {p_hand}, final score: {p_score}")
    print(f"Computer's final hand: {c_hand}, final score: {c_score}")
    if condition == "draw":
        print("Draw 🙃")
    elif condition == "computer_bj":
        print("Lose, opponent has Blackjack 😱")
    elif condition == "player_bj":
        print("Win with a Blackjack 😎")
    elif condition == "player_bust":
        print("You went over. You lose 😭")
    elif condition == "computer_bust":
        print("Opponent went over. You win 😁")
    elif condition == "win":
        print("You win 😃")
    elif condition == "lose":
        print("You lose 😤")
    else:
        print("You found a bug, please contact a developer ASAP!")


def blackjack():
    system('cls')
    print(logo)
    player_hand, computer_hand = deal_cards()
    more_cards = True
    win_condition = None
    player_score = calculate_score(player_hand)

    while more_cards:
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        win_condition = check_end_game(player_hand, computer_hand)
        if win_condition is None:
            want_more_cards = get_user_input()
            if want_more_cards == 'y':
                player_hand = draw_a_card(player_hand)
                player_score = calculate_score(player_hand)
            else:
                more_cards = False
        else:
            more_cards = False
    check_winner(player_hand, player_score, computer_hand, win_condition)
    more_game = input("Type 'y' if you want to play another! \n").lower()
    if more_game == 'y':
        blackjack()


blackjack()
