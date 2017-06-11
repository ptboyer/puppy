
from termcolor import colored
from ..api import pip, venv, puppy

PIN_DEFAULT = '-'
PIN_IS_SAVED = '*'
PIN_IS_DEVELOP = '%'
COLOUR_IS_SAVED = 'magenta'
COLOUR_IS_DEVELOP = 'cyan'

@venv.required
def cmd_list(args):

    config = puppy.read()
    dependencies = config.get('dependencies', {})

    for package in pip.get_packages():

        name = package.get('name', '').lower()
        version = package.get('version')

        pin = PIN_DEFAULT
        color = None
        is_saved = bool(dependencies.get(name))

        if is_saved:
            color = COLOUR_IS_SAVED
            pin = colored(PIN_IS_SAVED, COLOUR_IS_SAVED)
        elif version == 'develop':
            pin = colored(PIN_IS_DEVELOP, COLOUR_IS_DEVELOP)

        _pin = pin
        _name = colored(name, color, attrs=['bold'])
        _version = version

        _package = ('{pin} {name}@{version}'.format(
            name=_name, version=_version, pin=_pin))

        print(_package)

    puppy.test()
