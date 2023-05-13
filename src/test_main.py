import sys
print(sys.executable)
import pytest

from todo_app import *

def test_check_empty_tasks():
    todo_list = {}
    # Expect the function to return true because there are no tasks
    assert check_empty_tasks(todo_list) == True

    # Expect the function to return false because there is at least one task
    todo_list = {'Task1': '[X]'}
    assert check_empty_tasks(todo_list) == False

    # Multiple task should return false
    todo_list = {'Task1': '[X]', 'Task2': '[X]', 'Task3': '[X]'}
    assert check_empty_tasks(todo_list) == False


    # Check if the program exists without any errors
def test_menu(monkeypatch):
    # Mock the input as '5'
    monkeypatch.setattr('builtins.input', lambda _: '5')
    # Check if the menu function raises a SystemExit exception. If the exception is raised, it means that the program has exited as expected.
    with pytest.raises(SystemExit):
        menu()
    
    # Simulates the scenario where the task 'Task1' is already marked as finished
def test_not_finished_task_mark_unfinished(monkeypatch):
    global todo_list, not_finished_tasks, finished_tasks
    # Case1
    todo_list = {'Task1': '[\u2713]'}
    not_finished_tasks = []
    finished_tasks = ['Task1']
    # Mock input, Select the task to mark as unfinished
    monkeypatch.setattr('builtins.input', lambda _: 'Task1') 
    
    finished_task()
    
    # Assert that the task status is marked as unfinished
    assert todo_list['Task1'] == '[\u2713]'  
     # Assert that the task is in the not_finished_tasks list
    assert 'Task1' not in not_finished_tasks 
    assert 'Task1' in finished_tasks 


    # Case 2
    todo_list = {'Task2': '[X]'}
    not_finished_tasks = ['Task2']
    finished_tasks = []
    
    # Select the task to mark as unfinished
    monkeypatch.setattr('builtins.input', lambda _: 'Task2')  
    
    not_finished_task()
    
    # Assert that the task status remains unchanged
    assert todo_list['Task2'] == '[X]' 
    # Assert that the task is still in the not_finished_tasks list 
    assert 'Task2' in not_finished_tasks  
    # Assert that the task is not in the not_finished_tasks list 
    assert 'Task2' not in finished_tasks
