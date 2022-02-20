from game_settings import DifficultyRules
from statistics import Statistics
from game import game

statistics = Statistics()
difficulty_rules = DifficultyRules()

is_on = True

while is_on:
    options = difficulty_rules.get_difficulties()
    choice = input(f"Choose difficulty - {options} ").lower()

    if choice == 'off':
        is_on = False
    elif choice == 'info' or choice == 'information':
        statistics.info()
    elif choice == 'dev_update':
        statistics.update_info(int(input('wins: ')), int(input('loss: ')))
    elif difficulty_rules.get_name(choice):
        game(choice)
    else:
        print('No command found')
