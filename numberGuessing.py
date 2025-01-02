##You are required to build a simple number guessing game where the computer randomly selects a number and the user has to guess it. 
# The user will be given a limited number of chances to guess the number. 
# If the user guesses the number correctly, the game will end, and the user will win. 
# Otherwise, the game will continue until the user runs out of chances.


import random
import argparse

def computerNumber():
    num = random.randint(1, 100)
    return num

def gameLength(tries):
    while(tries != 0):
        print(f"okay cool, a random number was generated from the computer. guess the number you have {tries} left")
        userNumber = int(input("guess number: "))
        if userNumber == computerNumber():
            return "you win !!"
        else:
            "keep going"
        tries -= 1


       




def main():
    print("Welcome to number Guessing Game")
    print("Select a level difficulty as follows")
    print("for Easy press 1")
    print("for Medium press 2")
    print("for Hard press 3")
    levelDifficulty = int(input("select difficulty: "))
    ## based on level difficulty thats how you would loop the game
    if levelDifficulty == 1:
        tries = 10
        gameLength(tries)
    elif levelDifficulty == 2:
        tries = 5
        gameLength(tries)
    else:
        tries = 3
        gameLength(tries)
    
    print("thansk for playoing")

    

    
if __name__ == "__main__":
    main()