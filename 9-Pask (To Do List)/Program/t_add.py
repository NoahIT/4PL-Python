import Gfile

def registrate_task():
    for i in range(Gfile.dyd):
        print("> Enter your task name:\n")
        print(input(Gfile.task[i]))
        print("\n")
        print("> (OPTIONAL) Enter your subtask name:\n")
        print(input(Gfile.subtask[i]))
        print("\n")
        print("> (OPTIONAL) Enter your task required time to finish:\n")
        print(input(Gfile.time[i]))
        print("\n")
        print("> (OPTIONAL) Enter your task required day to finish:\n")
        print(input(Gfile.day[i]))
        print("\n")
        print("> (OPTIONAL) Enter your task prioritization:\n")
        print(input(Gfile.prioritization[i]))
        print("\n")
        print("[Task registered successfully]")
        Gfile.dyd = Gfile.dyd + 1
