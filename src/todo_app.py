from colorama import Fore
from tabulate import tabulate
import json
from datetime import datetime

# Define dictionaries to store tasks
todo_list = {}           # Stores tasks with their status and due date
finished_tasks = []      # Stores the names of finished tasks
not_finished_tasks = []  # Stores the names of unfinished tasks

# Function to display tasks and their statuses
def view_tasks():
    print('Number of tasks: ' + str(len(todo_list)))
    print(Fore.GREEN + 'Number of finished tasks: ' + str(len(finished_tasks)))
    print(Fore.RED + 'Number of unfinished tasks: ' + str(len(not_finished_tasks)))
    print(Fore.RESET)
    print('** [TASKS] **')
    print(f'Unfinished tasks: {not_finished_tasks}')
    print(f'Finished tasks: {finished_tasks}')

    for n, (task_name, task_details) in enumerate(todo_list.items()):
        status = task_details['status']
        if status == '[\u2713]':
            print(str(n + 1) + ') ' + status + ' ' + task_name + f' (Due: {task_details["due_date"]})')
        elif status == '[X]':
            print(str(n + 1) + ') ' + status + ' ' + task_name + f' (Due: {task_details["due_date"]})')
    print('\n')

    display()
    save_tasks_to_json()

# Load tasks from a .json file if it exists
try:
    with open('tasks.json', 'r') as json_file:
        data = json.load(json_file)
        todo_list = data.get('todo_list', {})
        finished_tasks = data.get('finished_tasks', [])
        not_finished_tasks = data.get('not_finished_tasks', [])
except FileNotFoundError:
    todo_list = {}
    finished_tasks = []
    not_finished_tasks = []

# Save tasks into the .json file
def save_tasks_to_json():
    data = {
        'todo_list': todo_list,
        'finished_tasks': finished_tasks,
        'not_finished_tasks': not_finished_tasks,
    }
    with open('tasks.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Display tasks and status in a table
def display():
    tasks = []
    for task_name, task_details in todo_list.items():
        status = task_details['status']
        tasks.append([status, task_name])

    headers = ["Status", "Task"]

    print(tabulate(tasks, headers=headers, tablefmt="fancy_grid"))

# Function to add a new task with a due date
def new_task():
    print(Fore.BLUE + '** NEW TASK **')
    print(Fore.RESET)
    while True:
        while True:
            new_task_name = input('Add new task or back to the menu(q): ')
            if new_task_name.lower() in todo_list:
                print('This name is already in use!')
                pass
            elif new_task_name == 'q':
                return
            else:
                break

        # Prompt the user for a due date
        while True:
            due_date_input = input('Enter the due date (YYYY-MM-DD) or leave empty: ')
            if not due_date_input:
                due_date = 'Not set'  # If the user leaves it empty, set it to 'Not set'
                break
            try:
                due_date = datetime.strptime(due_date_input, '%Y-%m-%d').strftime('%Y-%m-%d')
                break
            except ValueError:
                print('Invalid date format. Please use YYYY-MM-DD or leave it empty.')

        todo_list[new_task_name.lower()] = {
            'status': '[X]',
            'due_date': due_date,  # Include the due date in the task details
        }

        not_finished_tasks.append(new_task_name.lower())
        print('New task added to the list!')

 # Remove task from todo_list
def remove_task():
    print(Fore.RED + '** REMOVE TASK **')
    print(Fore.RESET)
    view_tasks()
    if len(todo_list) == 0:
        print('There is no task to remove')
        menu()
    while True:
        while True:
            remove_task_name = input('Which task would you like to remove? or back to menu(q): ')
            if remove_task_name == 'q':
                menu()
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


# Check if todo_list empty
def check_empty_tasks(todo_list):

    if len(todo_list) == 0:
        print('You have no task')
        return True
    return False

# Mark task as finished
def finished_task():
    print(Fore.GREEN + '** FINISHED TASK **')
    print(Fore.RESET)
    view_tasks()
    if check_empty_tasks(todo_list):
        return
    while True:
        while True:
            task_to_finish = input('Which task have you finished? or back to menu(q): ')
            if task_to_finish in todo_list:
                break
            elif task_to_finish == 'q':
                menu()
            else:
                print("Can't find it. Check correct task name")

        try:
            # Mark the task as finished by updating the status
            todo_list[task_to_finish]['status'] = '[\u2713]'
            not_finished_tasks.remove(task_to_finish)
            finished_tasks.append(task_to_finish)
            print('Task finished!')
        except:
            print('This task already finished!')

# Mark task as unfinished
def not_finished_task():
    print(Fore.YELLOW + '** UNFINISHED TASK **')
    print(Fore.RESET)
    view_tasks()
    if check_empty_tasks(todo_list):
        return
    while True:
        while True:
            task_to_unfinished = input('Which task have you not finished? or back to menu(q): ')
            if task_to_unfinished in todo_list:
                break
            elif task_to_unfinished == 'q':
                menu()
            else:
                print("Can't find task. Try again!")

        try:
            # Mark the task as unfinished by updating the status
            todo_list[task_to_unfinished]['status'] = '[X]'
            finished_tasks.remove(task_to_unfinished)
            not_finished_tasks.append(task_to_unfinished)
            print('Task uncompleted')
        except:
            print('You already uncompleted this task!')

# Display the menu and handle input
def menu():
    while True:
        view_tasks()
        print('\n', Fore.BLUE + '(1) Add Task\n', Fore.RED + '(2) Remove Task\n', Fore.GREEN + '(3) Finished Task\n', Fore.YELLOW + '(4) Un-finished Task\n', Fore.RESET + '(5) Exit\n')

        menu_choice = input('')
        if menu_choice == '1':
            new_task()
        elif menu_choice == '2':
            remove_task()
            return
        elif menu_choice == '3':
            finished_task()
        elif menu_choice == '4':
            not_finished_task()
        elif menu_choice == '5':
            exit()