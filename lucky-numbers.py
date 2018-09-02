"""
Lucky Numbers
Author: Leo Haris

Hint: Lucky Numbers are 21, 28, 35, 42, 49, 56, 63, 70, 77, 84
"""
import random

x = 5
y = 2
z = 7

# Ask user for a number
print("Enter a lucky whole number between 1 and 99: ")
user_input = int(input())

# calculate total using a random integer
total = (random.randint(1, 10) + y) * z

# Is total greater than user input?
if user_input > total:
    print("Sorry, user input is greater than total")
elif user_input == total:
    print("Lucky! User input is the same as the total")
else:
    print("Sorry, user input is less than total")

print("Total is " + str(total) + ", and user input was " + str(user_input))
