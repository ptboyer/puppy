
import os
from .io import IO
from .console import info, success
from .constants import VENV_NAME, VENV_PATH

io = IO(
    path='{}/bin'.format(VENV_NAME),
    targets=['pip', 'python'])


def exists():
    return os.path.exists(VENV_PATH)

def required(f):
    def wrapper(*args, **kwargs):
        if not exists():
            raise Exception(
                'No virtual environment exists.'
                '\n  Use `pup install` to create one.')
        return f(*args, **kwargs)
    return wrapper


def init():
    if not exists():
        command = 'virtualenv -p python3 {}'.format(VENV_NAME)
        for line in io.shell(command, virtual=False):
            print(info(line))
        print(success("Virtual Environemnt '{}' created".format(VENV_NAME)))
