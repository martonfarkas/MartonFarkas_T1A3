from colorama import Fore

todo_list = {}

finished_tasks = []
not_finished_tasks = []

no_tasks = False

def view_tasks():
    print('Number of tasks: ' + str(len(todo_list)))
    print(Fore.GREEN + 'Number of finished tasks: ' + str(len(finished_tasks)))
    print(Fore.RED + 'Number of unfinished tasks: ' + str(len(not_finished_tasks)))
    print('** [TASKS] **')
    print(Fore.RESET)
    print(f'Unfinished tasks: {not_finished_tasks}')
    print(f'Finished tasks: {finished_tasks}')

    for n, i in enumerate(todo_list):
        if todo_list[i] == '[\u2713]':
            print(str(n + 1) + ') ' + todo_list[i] + ' ' + i)
        elif todo_list[i] == '[X]':
            print(str(n + 1) + ') ' + todo_list[i] + ' ' + i)
    print('\n')

def new_task():
    print('** NEW TASK **')
    while True:
        while True:
            new_task_name = input('Add new task or back to menu(q): ')
            if new_task_name.lower() in todo_list:
                print('This name already in use!')
                pass
            elif new_task_name == 'q':
                return
            else:
                break

        todo_list[new_task_name.lower()] = '[X]'
        print('New task added to list!')
        not_finished_tasks.append(new_task_name.lower())

def remove_task():
    print('** REMOVE TASK **')
    view_tasks()
    if len(todo_list) == 0:
        print('There is no task to remove')
    while True:
        while True:
            remove_task_name = input('Which task would you like to remove? or back to menu(q): ')
            if remove_task_name == 'q':
                pass
            elif remove_task_name in todo_list:
                del todo_list[remove_task_name]
                print('Task removed')
                try:
                    finished_tasks.remove(remove_task_name)
                except:
                    not_finished_tasks.remove(remove_task_name)
                break
            else:
                print("Can't find this task. Did you typed correctly?")
                pass