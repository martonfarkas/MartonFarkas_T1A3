todo_list = {}

finished_tasks = []
not_finished_tasks = []

no_tasks = False

def view_tasks():
    print('Number of tasks: ' + str(len(todo_list)))
    print('Number of finished tasks: ' + str(len(finished_tasks)))
    print('Number of unfinished tasks: ' + str(len(not_finished_tasks)))
    print('** TASKS **')
    print(f'Unfinished tasks: {not_finished_tasks}')
    print(f'Finished tasks: {finished_tasks}')