from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")


def main():
    while True:
        # Get user input and strip space from it
        print(now)
        user_action = input("Type add, show, edit, complete or exit: ").strip()

        if user_action.startswith("add"):
            todo = user_action[4:].capitalize()
            if len(todo) < 2:
                continue
            todos = get_todos()
            todos.append(todo + '\n')

            write_todos(todos)

        elif user_action.startswith("show"):
            todos = get_todos()
            for i, value in enumerate(todos):
                value = value.strip('\n')
                print(f"{i + 1} - {value}")

        elif user_action.startswith("edit"):
            try:
                todos = get_todos()

                number = int(user_action[5:]) - 1
                if number > len(todos) - 1:
                    print(f"There are only {len(todos)} todos. Please enter a valid number.")
                else:
                    new_todo = input("Enter new todo: ").capitalize() + "\n"
                    todos[number] = new_todo
                    write_todos(todos)
            except ValueError:
                print("You should enter the number of todo!")
                continue
        elif user_action.startswith("complete"):
            try:
                number = int(user_action[9:])
                todos = get_todos()
                if number > len(todos):
                    print(f"There are only {len(todos)} todos. Please enter a valid number.")
                else:
                    deleted = todos.pop(number - 1).strip('\n')
                    write_todos(todos)
                    message = f"Todo - {deleted} was removed from the list."
                    print(message)
            except Exception as ex:
                print(ex)
                continue
            # Exit from loop
        elif user_action.startswith("exit"):
            break
        else:
            print("Command is not valid. Try again!")


if __name__ == '__main__':
    main()
