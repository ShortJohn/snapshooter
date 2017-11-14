import os.path


def check_directory_exists(path):
    """
    Checks whether the directory exists
    :param path:
    :return:
    """
    dir = os.path.dirname(path)
    exists = os.path.exists(dir)
    return exists