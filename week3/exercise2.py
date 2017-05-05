"""Week 3, Exercise 2.

An example of how a guessing game might be written.
"""
from __future__ import division
from __future__ import print_function
import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nwelcome to the guessing game!")
    upperBound = raw_input("Enter an upper bound: ")
    lowerBound = raw_input("Enter a lower bound: ")
    print("OK then, a number between {} and {} ?".format(upperBound,
                                                         lowerBound))
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(raw_input("guess a number: "))
        print("you guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
