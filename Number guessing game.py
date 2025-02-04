from random import randint
import math

lower = int(input("Enter the lower number: "))
higher = int(input("Enter the higher number: "))

Random_Number = randint(lower, higher)
try:
    Total_Chances = math.ceil(math.log(higher - lower + 1, 2))
except ValueError:
    print("Please enter it correct")


print(f"\tIt's ready you've {Total_Chances} chances please enter a number from {lower} to {higher}:\n")

Guesses = 0
while Total_Chances > Guesses:
    Guesses += 1
    User_Number = int(input("Guess a number: "))
    
    if User_Number == Random_Number:
        print(f"That's right from the {Guesses} try")
        exit()
    elif User_Number < Random_Number:
        print("You guessed too small!")
    elif User_Number > Random_Number:
        print("You Guessed too high!")

print(f"\nYou lost the number was {Random_Number} \n\tBetter luck next time!")