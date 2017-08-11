
from ..api import puppy, venv, pip
from ..api.console import meta, warn, error
from ..api.packages import format_package_names, string_package_names
from ..api.venv import io
from ..api.pip_parse import (
    ACTION_UNINSTALLING,
    parse_line
)
from .install import render_line

def print_uninstalling():
    print('🐶  Uninstalling packages')

def print_uninstalling_sucess(packages):
    print('🎾  Successfully uninstalled packages ({})'.format(
        meta(packages)))

def pip_uninstall(packages):
    for line in io.shell('/usr/bin/yes | pip uninstall {}'.format(packages)):
        res = parse_line(line)
        action = res.get('action')
        if action == ACTION_UNINSTALLING:
            print(render_line(line, res))

@venv.required
def cmd_uninstall(args):

    target = args.target
    if not target:
        raise Exception('No packages specified.')

    config = puppy.read()
    packages = format_package_names(target)

    all_packages = {}
    for package in pip.get_packages():
        all_packages[package.get('name', '').lower()] = package

    # uninstall the packages through pip
    print_uninstalling()

    # check that package exists either in freeze or pupfile
    successful_packages = []
    for package in packages:
        is_installed = bool(all_packages.get(package))
        is_saved = bool(config.get('dependencies', {}).get(package))

        if not is_installed:
            print(error("Package '{}' is not installed!".format(
                package)))
        else:
            if pip_uninstall(package):
                successful_packages.append(package)
            else:
                print(warn("Package '{}' failed to uninstall!".format(
                    package)))

        if args.save and not is_saved:
            print(warn("Package '{}' is not a saved dependency!".format(
                package)))

    successful_packages_string = string_package_names(successful_packages)
    if successful_packages_string:
        print_uninstalling_sucess(successful_packages_string)

    if args.save:
        # add versions to pupfile after installations
        if not puppy.test():
            return

        for package in packages:
            if config['dependencies'].get(package):
                config['dependencies'].pop(package)

        puppy.write(config)
