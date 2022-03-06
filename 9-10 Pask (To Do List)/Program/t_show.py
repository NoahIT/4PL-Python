import Gfile

""" Prints all or individual task properties to console """

def show_all_tasks():
    for i in range(Gfile.dyd):
        print("[",i," Task]\n")
        print("\tTask name: ",Gfile.task[i],"\n")
        print("\tTask subtask: ", Gfile.subtask[i],"\n")
        print("\tTask time: ", Gfile.time[i],"\n")
        print("\tTask day: ", Gfile.day[i],"\n")
        print("\tTask prioritization: ", Gfile.prioritization[i],"\n\n")

def show_task_names():
    for i in range(Gfile.dyd):
        print("[",i,"] Task name: ",Gfile.task[i],"\n")

def show_individual_task():
    print("Enter the index of the task you want to get more information about: ")
    input(Gfile.t_num)
    i = Gfile.t_num
    print("\n")
    print("\tTask name: ", Gfile.task[i], "\n")
    print("\tTask subtask: ", Gfile.subtask[i], "\n")
    print("\tTask time: ", Gfile.time[i], "\n")
    print("\tTask day: ", Gfile.day[i], "\n")
    print("\tTask prioritization: ", Gfile.prioritization[i], "\n\n")

