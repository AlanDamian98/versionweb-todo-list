FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """leer un archivo de texto y returns la lista de work pending"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write la lista de work pending en el archivo de texto"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
