
from .venv import pip

def index_pip_packages():
    # get all package versions from pip freeze
    res = pip('freeze')
    if res.returncode != 0:
        raise Exception('Failed to access version information.')

    # index all package versions into dict
    freeze = res.stdout.decode('utf-8').splitlines()
    versions = {}
    for package in freeze:
        name, version = package.split('==')
        versions[name.lower()] = version

    return versions
