import global_variables
import question

def start_up(self):
    print("|==--  Welcome to Quiz game engine  --==|")
    print("|==--                               --==|")
    print("|==-- Let's start the quiz (YES/NO) --==|")
    global_variables.start = input("Enter here: ")

    if global_variables.start == "YES":
        question.S_question.print_question(tuple)
    elif global_variables.start == "NO":
        print("\nGoodbye !")
        exit()
    else:
        print("\n!!! Invalid value, Please enter YES (Start the quiz) or NO (Exit) !!!\n\n")
        start_up(tuple)

start_up(tuple)