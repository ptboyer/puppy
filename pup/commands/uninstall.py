
from ..api.venv import use_venv, requires_venv, pip
from ..api.pupfile import read_pupfile, write_pupfile, test_pupfile
from ..api.packages import format_package_names, string_package_names
from ..api.console import meta, warn
from ..api.piputil import index_pip_packages

def print_uninstalling(packages):
    print('🐶  Uninstalling packages ({})'.format(
        meta(packages)))

def print_uninstalling_sucess(packages):
    print('🎾  Successfully uninstalled packages ({})'.format(
        meta(packages)))

def pip_uninstall(packages):
    res = pip('uninstall {}'.format(packages), pre='/usr/bin/yes | ')
    if res.returncode != 0:
        return False
    return True

@requires_venv
def cmd_uninstall(args):

    use_venv()

    target = args.target
    if not target:
        raise Exception('No packages specified.')

    config = read_pupfile()
    packages = format_package_names(target)
    freeze = index_pip_packages()

    # uninstall the packages through pip
    packages_string = string_package_names(packages)
    print_uninstalling(packages_string)

    # check that package exists either in freeze or pupfile
    successful_packages = []
    for package in packages:
        is_installed = bool(freeze.get(package))
        is_saved = bool(config['dependencies'].get(package))
        if not is_installed:
            print(warn('Package ({}) is not installed!'.format(
                package)))
        if args.save and not is_saved:
            print(warn('Package ({}) is not a saved dependency!'.format(
                package)))
        if is_installed or (args.save and is_saved):
            if pip_uninstall(package):
                successful_packages.append(package)
            else:
                print(warn('Package ({}) failed to uninstall!'.format(
                    package)))

    successful_packages_string = string_package_names(successful_packages)
    if successful_packages_string:
        print_uninstalling_sucess(successful_packages_string)

    if args.save:
        # add versions to pupfile after installations
        if not test_pupfile():
            return

        for package in packages:
            if config['dependencies'].get(package):
                config['dependencies'].pop(package)

        write_pupfile(config)
