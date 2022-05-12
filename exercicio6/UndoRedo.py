# Undo e Redo

def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()

def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada para desfazer.')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada para refazer.')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)

def do_add(todo, todo_list):
    todo_list.append(todo)

if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma nova tarefa ou desfazer, refazer, lista: ')

        if todo == 'lista':
            show_op(todo_list)
            continue
        elif todo == 'desfazer':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'refazer':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)