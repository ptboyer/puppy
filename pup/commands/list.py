
from termcolor import colored
from ..api.venv import requires_venv, pip
from ..api.pupfile import read_pupfile, test_pupfile

@requires_venv
def cmd_list(args):

    config = read_pupfile()
    dependencies = config.get('dependencies', {})
    versions = {}

    # get all package versions from pip freeze
    res = pip('freeze')
    if res.returncode != 0:
        raise Exception('Failed to access version information.')

    # index all package versions into dict
    freeze = res.stdout.decode('utf-8').splitlines()
    versions = {}
    for package in freeze:
        name, version = package.split('==')
        _package = name.lower()
        versions[_package] = version

        # print package versions, mark those included in dependencies
        pin = bool(dependencies.get(_package))
        out = ('{pin} {name}@{version}'.format(
            name=colored(_package, attrs=['bold']),
            version=versions.get(_package),
            pin='*' if pin else '-'))

        if pin:
            print(colored(out, 'magenta'))
        else:
            print(out)

    test_pupfile()
