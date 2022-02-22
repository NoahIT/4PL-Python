import Gfile #Global variable files

class Task:
    """ Task object """

    def __init__(self, task, subtask, time, day, prioritization):
        self.task = task[Gfile.dyd]
        self.subtask = subtask[Gfile.dyd]
        self.time = time[Gfile.dyd]
        self.day = day[Gfile.dyd]
        self.prioritization = prioritization[Gfile.dyd]

    def change_task(self, task, subtask, time, day, prioritization):
        self.task = task[Gfile.dyd]
        self.subtask = subtask[Gfile.dyd]
        self.time = time[Gfile.dyd]
        self.day = day[Gfile.dyd]
        self.prioritization = prioritization[Gfile.dyd]

    def get_task_info(self):
        """ Show chosen tasks attributes """

        for i in range(Gfile.dyd):
            print("> To See information about all tasks [ENTER 1]")
            print("> To See information about one task  [ENTER 0]\n")
            input(Gfile.num)
            print("\n")
            if Gfile.num == 1:
                for i in range(Gfile.dyd):
                    print(f"Task name: \t\t{self.task[i]}\n")
                    print(f"Task subtask: \t{self.subtask[i]}\n")
                    print(f"Task time: \t\t{self.time[i]}\n")
                    print(f"Task day: \t{self.subtask[i]}\n")
                    print(f"Task Prioritization: \t\t{self.prioritization[i]}\n")
            elif num == 0:
                print("Enter the index of the task you want to get more information about: ")
                input(i)
                print("\n")
                print(f"Task name: \t\t{self.task[i]}\n")
                print(f"Task subtask: \t{self.subtask[i]}\n")
                print(f"Task time: \t\t{self.time[i]}\n")
                print(f"Task day: \t{self.subtask[i]}\n")
                print(f"Task Prioritization: \t\t{self.prioritization[i]}\n")
            else:
                print("! Invalid input number !\n")