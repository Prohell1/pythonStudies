num_char = len(input("What is your name?\n"))  # input always stores the data as integer
new_num_char = str(num_char)  # we convert the integer to string to be able to concatenate with it
print("Your name has " + new_num_char + " characters.")  # this way we avoid Type Errors

a = float(123)
print(type(a))  # Result is float, because we converted an integer into float

print(70 + float("100.5"))  # prints 170.5
print(str(70) + str(100))  # prints 70100
