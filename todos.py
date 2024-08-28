def access_todos(action, payload=None, filepath="todos.txt"):
    """access a lisf of todos from a file with read or write action"""
    if payload is not None and len(payload) > 0:
        with open(filepath, "w") as file:
            file.writelines(payload)
        return None  # Return None explicitly when writing
    else:
        with open(filepath, action) as file:
            return file.readlines()