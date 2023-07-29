import os
from art import logo

print(logo)
print("Welcome to the secret auction program. ")
bidders = {}
continue_bidding = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    os.system('cls')
    if more_bidders != "yes":
        continue_bidding = False
        find_highest_bidder(bidders)





