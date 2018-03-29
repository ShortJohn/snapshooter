import os.path


def file_exists(file):
    exists = os.path.isfile(file)
    return exists
