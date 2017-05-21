
import os
import subprocess
from .constants import VENV_NAME, VENV_PATH

def requires_venv(f):
    def wrapper(*args, **kwargs):
        if not os.path.exists(VENV_PATH):
            raise Exception(
                'No virtual environment exists.'
                '\n  Use `pup install` to create one.')
        return f(*args, **kwargs)
    return wrapper

def check_venv():
    return os.path.exists(VENV_PATH)

def use_venv():
    if not check_venv():
        subprocess.run(
            ['virtualenv -p python3 {} &> /dev/null'.format(
                VENV_NAME)],
            shell=True, check=True)

def pip(args, pre=''):

    return subprocess.run(
        ['{}{}/bin/pip {}'.format(
            pre, VENV_NAME, args)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)

def python(args='', pre=''):

    return subprocess.run(
        ['{}{}/bin/python {}'.format(
            pre, VENV_NAME, args)],
        shell=True)

def script(command):

    command = command.replace('python', '{}/bin/python'.format(VENV_NAME))
    return subprocess.run([command], shell=True)
