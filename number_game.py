#!/bin/bash

import random

def generate_random_number() -> int:
    random_number: int = random.randint(1, 100)
    return random_number


def tries_difficulty_level(level: int) -> int:
    if level == 1:
        return 10
    elif level == 2:
        return 5
    elif level == 3:
        return 3
    else:
        print("choose a valid difficulty level")
        return ""

def user_guess() -> int:
    user_number = input("What number is the computer thinking of? Input a number between 1 and 100: ")
    return int(user_number)


level = input("Choose the difficulty level\n1 for easy"
                "\n2 for medium \n3 for hard")
tries = tries_difficulty_level(int(level))

random_number = generate_random_number()
print(random_number)
for t in range(tries):
    user_number = user_guess()
    if user_number == random_number:
        print("you win")
        exit(0)
    elif user_number > random_number:
        print("your number is greater than the computer's number")
    else:
        print("your number is smaller than the computer's number")
print("you lose")


