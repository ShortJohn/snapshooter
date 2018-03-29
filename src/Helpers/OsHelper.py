import subprocess


class OsResult:

    def __init__(self, out, err):
        self.out = out
        self.err = err


def run_command(command):
    result = None
    try:
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = result.communicate()
        osResult = OsResult(out, err)
    except OSError:
        print("Failed to execute command")
        osResult = OsResult("", "-1")

    return osResult


def run_command_with_exception_on_error(command):
    result = None
    try:
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = result.communicate()
        osResult = OsResult(out, err)
    except OSError:
        command = ' '.join(command)
        raise Exception("Failed to execute command" + command)

    return osResult
