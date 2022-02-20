from game_settings import DifficultyRules
from statistics import Statistics
import random
import math

statistics = Statistics()
difficulty_rules = DifficultyRules()


def game(difficulty):
    lower = 0
    upper = 10

    randomint = random.randint(lower, upper)
    myguesses = 0
    health = difficulty_rules.get_health(difficulty)
    while myguesses < health:
        myguesses += 1
        guess = int(input("Guess a number: "))
        if guess == randomint:
            print("Congratulations you did it in ",
                  myguesses, " try")
            statistics.update_win()
            break
        elif guess < randomint:
            print("You guessed too small!")
        elif guess > randomint:
            print("You Guessed too high!")

    if myguesses >= health:
        statistics.update_loss()
        print("\nThe number is %d" % randomint)
        print("\nBetter Luck Next time!")
