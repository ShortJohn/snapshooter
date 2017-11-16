import os.path
import sys

__all__ = ['check_directory_exists', 'get_url_from_command_line', 'get_screenshot_save_path_from_command_line']


def check_directory_exists(path):
    """
    Checks whether the directory exists
    :param path:
    :return:
    """
    dir = os.path.dirname(path)
    exists = os.path.exists(dir)
    return exists


def get_url_from_command_line():
    url = sys.argv[1]
    return url


def get_screenshot_save_path_from_command_line():
    path = sys.argv[2]
    return path
