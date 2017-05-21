
from ..api.venv import use_venv, check_venv, pip
from ..api.pupfile import read_pupfile, write_pupfile, test_pupfile
from ..api.packages import format_package_names, string_package_names
from ..api.console import meta, warn
from ..api.constants import VENV_NAME
from ..api.piputil import index_pip_packages

def print_fetching(packages):
    if packages:
        print('🐶  Fetching packages ({})'.format(
            meta(packages)))
    else:
        print('🐶  No packages to fetch!')

def print_fetching_success(packages):
    if packages:
        print('🎾  Successfully installed packages ({})'.format(
            meta(packages)))

def pip_install(packages):
    res = pip('install {}'.format(packages))
    if res.returncode != 0:
        raise Exception(
            (b'Failed to install.\n' + res.stderr).decode("utf-8"))


def install_all(args):

    if not test_pupfile():
        return

    config = read_pupfile()
    dependencies = config.get('dependencies', {})

    packages = []
    for package in dependencies:
        packages.append('{}=={}'.format(
            package, dependencies[package]))

    # install all dependencies through pip
    packages_string = string_package_names(packages)
    print_fetching(packages_string)
    pip_install(packages_string)
    print_fetching_success(packages_string)

def install_targets(args):

    use_venv()

    config = read_pupfile()
    packages = format_package_names(args.target)
    freeze = index_pip_packages()

    # install all packages through pip
    packages_string = string_package_names(packages)
    print_fetching(packages_string)
    pip_install(packages_string)
    print_fetching_success(packages_string)

    for package in packages:
        if bool(freeze.get(package)):
            print(warn('Package ({}) already installed!'.format(
                package)))

    if args.save:
        # add versions to pupfile after installations
        if not test_pupfile():
            return

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

        # update pupfile dependencies with installed packages versions
        for package in packages:
            config['dependencies'][package] = versions[package]

        write_pupfile(config)

def cmd_install(args):

    # output the status of the virtual environment
    if check_venv():
        print('📦  Using existing virtual environment ({})'.format(
            meta(VENV_NAME)))
    else:
        print('📦  Creating new virtual environment ({})'.format(
            meta(VENV_NAME)))

    # ensure the virtual environment exists
    use_venv()

    # install the packages
    if args.target:
        install_targets(args)
    else:
        install_all(args)
