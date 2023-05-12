import sys
print(sys.executable)
import pytest
from todo_app import check_empty_tasks
from todo_app import menu

def test_check_empty_tasks():
    todo_list = {}
    assert check_empty_tasks(todo_list) == True

    todo_list = {'Task1': '[X]'}
    assert check_empty_tasks(todo_list) == False



def test_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')

    with pytest.raises(SystemExit):
        menu()