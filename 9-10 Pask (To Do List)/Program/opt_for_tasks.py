from t_add import registrate_task
from t_edit import edit_task
from t_delete import delete_task
from t_get_info import get_task_info
import Gfile

def options():
    print("> Add Task                 [ENTER 0]\n")
    print("> Edit Task                [ENTER 1]\n")
    print("> Delete Task              [ENTER 2]\n")
    print("> Get info about the Task  [ENTER 3]\n")

    input(Gfile.registration_option_num)

    if Gfile.registration_option_num == 0:
        registrate_task()
    elif Gfile.registration_option_num == 1:
        edit_task()
    elif Gfile.registration_option_num == 2:
        delete_task()
    elif Gfile.registration_option_num == 3:
        get_task_info()
    else:
        print("! Invalid input number !\n")


