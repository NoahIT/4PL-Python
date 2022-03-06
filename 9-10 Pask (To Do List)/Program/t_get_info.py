from t_show import show_all_tasks
from t_show import show_individual_task
import Gfile

""" Shows chosen tasks properties """

def get_task_info():
        print("> To See information about all tasks [ENTER 1]")
        print("> To See information about one task  [ENTER 0]\n")
        input(Gfile.num)
        print("\n")
        if Gfile.num == 1:
            show_all_tasks()
        elif Gfile.num == 0:
            show_individual_task()
        else:
            print("! Invalid input number !\n")