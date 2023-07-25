print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
result = round((total_bill + total_bill * (tip_amount / 100)) / people, 2)

print(f"Each person should pay: ${result}")
