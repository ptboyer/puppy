
from . import venv
from .pip_parse import (
    LS_EGG_PREFIX,
    parse_package
)

def get_packages():

    packages = []

    for line in venv.io.shell('pip freeze'):

        line = line.strip()

        if line.startswith('#'):
            continue

        package = parse_package(line)
        if not package.get('version'):
            if line.startswith('-e'):
                name = line[line.find(LS_EGG_PREFIX) + len(LS_EGG_PREFIX):]
                package['name'] = name
                package['version'] = 'develop'

        packages.append(package)

    return packages
