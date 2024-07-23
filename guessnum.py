# Guess a number

import random

def main():
    number_to_guess=random.randint(1,100)
    attempts=0
    guess=None
    
    print("guess the number (between 1 to 100):")
    
    while guess!=number_to_guess:
         guess=int(input("Enter your guess:"))
         attempts+=1
         
         if guess < number_to_guess:
             print("Too low! Try again.")
         elif guess > number_to_guess:
             print("Too high! Try again.")
         else:
             print("Congratulations!")
             print(f"The number of attempts you take is{attempts}.")
             
main()         
                 