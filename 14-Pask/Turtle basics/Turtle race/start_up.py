import turtle_race

start_up = True

def start():
    start = input('Would you like to play this race (enter yes/no): ')
    if start == 'yes':
        turtle_race.startGame1()
    elif start == 'no':
        print('\nGoodbye !')
        exit()
    else:
        print("\nSorry, that was an invalid command!")
        start()

def start_again():
    start = input("Would you like to play again (enter yes/no) ?: ")
    if start == 'yes':
        turtle_race.startGame1()
    elif start == 'no':
        print('\nGoodbye !')
        exit()
    else:
        print("\nSorry, that was an invalid command!")
        start()

start()