import global_variables

def select_level():
    print("|==--        Select Level:        --==|")
    print("|==--                             --==|")
    print("|==--            Easy             --==|")
    print("|==--           Medium            --==|")
    print("|==--            Hard             --==|")
    print("|==--                             --==|")
    global_variables.levels = input("Enter here: ")

    if global_variables.levels == "Easy":
        print("Easy level selected")
    elif global_variables.levels == "Medium":
        print("Medium level selected")
    elif global_variables.levels == "Hard":
        print("Hard level selected")
    else:
        print("Invalid name, please enter again")