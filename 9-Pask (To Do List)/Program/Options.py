from tasks import Task
import Gfile

class Add_Task(Task):
    """ Input Task name """

    for i in range(Gfile.dyd):
        print("> Enter your task name: ")
        Task[i] = input()
        print("\n")

        print("> (OPTIONAL) Enter your tasks subtask: ")
        Task[i] = input()
        print("\n")





