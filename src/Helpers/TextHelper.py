def string_starts_with(string, substring):
    """

    :param string:
    :param substring:
    """
    string = "" + string + ""
    substring = "" + substring + ""
    return string.startswith(substring)


def string_ends_with(string, substring):
    """

    :param string:
    :param substring:
    """
    string = "" + string + ""
    substring = "" + substring + ""
    return string.endswith(substring)


def string_contains(string, substring):
    """

    :param string:
    :param substring:
    """
    string = "" + string + ""
    substring = "" + substring + ""
    return substring in string


def get_string_between(string, from_string, to_string):
    """

    :param string:
    :param substring:
    """
    from_string = "" + from_string + ""
    to_string = "" + to_string + ""

    try:
        start = string.index(from_string) + len(from_string)
        end = string.index(to_string, start)
        return string[start:end]
    except ValueError:
        return None
