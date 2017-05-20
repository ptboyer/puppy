
import os
import shutil
import subprocess
import argparse
import json
from termcolor import colored


def requires_venv(f):
    def wrapper(self, *args):
        if not os.path.exists(self.VENV_PATH):
            raise Exception('No {} virtual environment exists.'.format(
                self.VENV_NAME))
        return f(self, *args)
    return wrapper


def creates_venv(f):
    def wrapper(self, *args):
        # create virtual environment if not exist
        self.venv()
        return f(self, *args)
    return wrapper


class PUP(object):

    def __init__(self):

        self.VENV_NAME = '.puppy'
        self.VENV_PATH = os.getcwd() + '/{}'.format(self.VENV_NAME)
        self.PUPFILE_NAME = 'puppy.json'

        parser = argparse.ArgumentParser(
            description='PUP Uncomplicates Packages')
        parser.add_argument(
            'command', metavar='command', type=str)
        parser.add_argument(
            'package', metavar='package', nargs='*', type=str)
        parser.add_argument(
            '--save', action='store_true', required=False)

        args = parser.parse_args()

        try:
            if args.command == 'install':
                if args.package:
                    self.add(args)
                else:
                    self.install()
            elif args.command == 'uninstall':
                self.uninstall(args)
            elif args.command == 'list':
                self.list()
            elif args.command == 'run':
                self.run(args)
            elif args.command == 'destroy':
                self.destroy()
            else:
                raise Exception('Not a valid command.')

            self.check_pupfile()

        except Exception as e:
            err = colored('ERR', 'red', attrs=['bold'])
            if (str(e).find('Failed to establish a new connection') != -1):
                e = 'Failed to establish network connection.'
            print('{} {}'.format(err, e))
            return exit(1)

        else:
            return exit(0)

    def read_pupfile(self):
        data = {}

        try:
            with open(self.PUPFILE_NAME, 'r') as f:
                data = json.load(f)
        except:
            pass

        if not data.get('dependencies'):
            data['dependencies'] = {}

        return data

    def write_pupfile(self, data):
        with open(self.PUPFILE_NAME, 'w') as f:
            json.dump(data, f, indent=2)

    def check_pupfile(self):
        try:
            open(self.PUPFILE_NAME, 'r')
        except:
            print('🗒  Package file not found! ({})'.format(
                colored(self.PUPFILE_NAME, 'grey', attrs=['bold'])))
        else:
            print('🗒  Package file checks out! ({})'.format(
                colored(self.PUPFILE_NAME, 'grey', attrs=['bold'])))

    def venv(self):

        if not os.path.exists(self.VENV_PATH):
            print('📦  Creating new virtual environment... ({})'.format(
                colored(self.VENV_NAME, 'grey', attrs=['bold'])))
            subprocess.run(
                ['virtualenv -p python3 {} &> /dev/null'.format(
                    self.VENV_NAME)],
                shell=True, check=True)
        else:
            print('📦  Using existing virtual environment... ({})'.format(
                colored(self.VENV_NAME, 'grey', attrs=['bold'])))

    @requires_venv
    def pip(self, args, pre=''):

        return subprocess.run(
            ['{}{}/bin/pip {}'.format(
                pre, self.VENV_NAME, args)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)

    @requires_venv
    def python(self, args):

        return subprocess.run(
            ['{}/bin/python {}'.format(
                self.VENV_NAME, args)],
            shell=True)

    @creates_venv
    def install(self):

        config = self.read_pupfile()
        dependencies = config.get('dependencies', {})

        packages = []
        for package in dependencies:
            packages.append('{}=={}'.format(
                package, dependencies[package]))

        _packages = ' '.join(packages)

        # install all dependencies through pip
        print('🐶  Fetching packages... ({})'.format(
            colored(_packages, 'grey', attrs=['bold'])))

        res = self.pip('install {}'.format(_packages))
        if res.returncode != 0:
            raise Exception(
                (b'Failed to install.\n'+res.stderr).decode("utf-8"))

    @creates_venv
    def add(self, args):

        config = self.read_pupfile()
        packages = args.package

        # convert all to lowercase
        packages = [package.lower() for package in packages]
        # create string feedable version of list
        _packages = ' '.join(packages)

        # install all packages through pip
        print('🐶  Fetching packages... ({})'.format(
            colored(_packages, 'grey', attrs=['bold'])))

        res = self.pip('install {}'.format(_packages))
        if res.returncode != 0:
            raise Exception(
                (b'Failed to install.\n'+res.stderr).decode("utf-8"))

        if args.save:
            # add versions to pupfile after installations

            # get all package versions from pip freeze
            res = self.pip('freeze')
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

            self.write_pupfile(config)

    @requires_venv
    def uninstall(self, args):

        target = args.package
        if not target:
            raise Exception('No packages specified.')

        config = self.read_pupfile()
        packages = args.package

        # convert all to lowercase
        packages = [package.lower() for package in packages]
        # create string feedable version of list
        _packages = ' '.join(packages)

        res = self.pip('uninstall {}'.format(_packages), pre='/usr/bin/yes | ')
        if res.returncode != 0:
            if res.stderr.decode('utf-8').find('not installed') == -1:
                raise Exception(
                    (b'Failed to uninstall.\n'+res.stderr).decode("utf-8"))

        if args.save:
            # add versions to pupfile after installations

            for package in packages:
                if config['dependencies'].get(package):
                    config['dependencies'].pop(package)

            self.write_pupfile(config)

    @requires_venv
    def list(self):

        config = self.read_pupfile()
        dependencies = config.get('dependencies', {})
        versions = {}

        # get all package versions from pip freeze
        res = self.pip('freeze')
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

    @requires_venv
    def run(self, args):

        target = args.package
        if not target:
            raise Exception('Target required.')

        # only concern the first arg
        target = target[0]

        return self.python(target)

    @requires_venv
    def destroy(self):

        shutil.rmtree(self.VENV_PATH)

PUP()
