from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is " + now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()



        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos = get_todos()
            todos[number] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("Your command is not valid!")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[number-1].strip('\n')
            todos = get_todos()
            todos.pop(number-1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Index is out of range")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("Bye!")