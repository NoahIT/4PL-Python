import global_variables
import question

def start_up(self):
    print("|==--                               --==|")
    print("|==--  Welcome to Quiz 2. Space invaders (Exam_2) engine  --==|")
    print("|==--                               --==|")
    print("|==-- Let's start the quiz (YES/NO) --==|")
    print("|==--                               --==|")
    global_variables.start = input("Enter here: ")

    if global_variables.start == "YES":
        question.S_question.print_question('self')
    elif global_variables.start == "NO":
        print("\nGoodbye !")
        exit()
    else:
        print("\n!!! Invalid value, Please enter YES (Start the quiz) or NO (Exit) !!!\n\n")
        start_up(tuple)

start_up('self')