#!/bin/bash

import random


random_number: int = random.randint(0, 100)

def select_difficulty_level() -> int:
    level = input("Choose the difficulty level\n1 for easy"
                   "\n2 for medium \3 for hard")
    if level == "1":
        return 10
    elif level == "2":
        return 5
    elif level == "3":
        return 3
    else:
        print("choose a valid difficulty level")
        return ""
    


