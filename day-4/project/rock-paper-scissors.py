import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
computerNum = random.randint(0, 2)
userNum = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computerChoice = choices[computerNum]
userChoice = choices[userNum]
winningMessage = "You win!"
tieMessage = "It is a draw!"
losingMessage = "You lose!"

print(f"You choose:\n {userChoice}")
print(f"Computer choose:\n {computerChoice}")

if userChoice == rock:
    if computerChoice == rock:
        print(tieMessage)
    elif computerChoice == paper:
        print(losingMessage)
    else:
        print(winningMessage)
elif userChoice == paper:
    if computerChoice == rock:
        print(winningMessage)
    elif computerChoice == paper:
        print(tieMessage)
    else:
        print(losingMessage)
else:
    if computerChoice == rock:
        print(losingMessage)
    elif computerChoice == paper:
        print(winningMessage)
    else:
        print(losingMessage)



