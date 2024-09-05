from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit,completed or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, i in enumerate(todos):
            i = i.strip('\n')
            i = i.title()
            row = f"{index + 1}-{i}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todos = input("Enter a new todo: ")
            todos[number] = new_todos + '\n'

            write_todos(todos)

        except ValueError:
            print("Enter the number after edit")
        except IndexError:
            print("your command is not valid")
            continue

    elif user_action.startswith("completed"):
        try:

            for index, i in enumerate(todos):
                i = i.strip("\n")
                i = i.title()
                row = f"{index + 1}-{i}"
                print(row)

            completed_no = int(user_action[10:])

            todos = get_todos()
            index = completed_no - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo -- {todo_to_remove} -- was removed from the list."
            print(message)
        except ValueError:
            print("Enter the number after completed.")
        except IndexError:
            print("The todo number entered is wrong.")
            continue

    elif user_action.startswith("exit"):
         break

    else:
        print("Command is not valid BITCH!!")

print("Bye!")
