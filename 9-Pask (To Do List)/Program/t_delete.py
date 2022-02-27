import Gfile


def delete_task():
    print("Enter the number of the task you want to delete: ")
    input(Gfile.t_num)
    i=Gfile.t_num
    print("\n")
    Gfile.task[i] = " "
    Gfile.subtask[i] = " "
    Gfile.time[i] = 0
    Gfile.day[i] = 0
    Gfile.prioritization[i] = " "