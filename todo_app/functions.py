PATH = "files/todo.txt"


def get_todos(filepath=PATH):
    """Read a text file and return the list of
    to-do items.
    :param filepath:
    """
    with open(filepath) as doc:
        todo_list = doc.readlines()
    return todo_list


def write_todos(our_file, filepath=PATH):
    """Write the to-do items list in the text file
    :param our_file:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as doc:
        todo_list = doc.writelines(our_file)
    return todo_list
