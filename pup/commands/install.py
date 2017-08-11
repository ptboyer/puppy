
from subprocess import CalledProcessError
from ..api import venv, puppy, pip
from ..api.venv import io
from ..api.pip_parse import (
    ACTION_COLLECTING,
    ACTION_CLONING,
    ACTION_INSTALLING_SUCCESS,
    ACTION_REQUIREMENT_PREEXISTS,
    ACTION_UNINSTALLING,
    parse_line,
    parse_package
)
from ..api.packages import format_package_names, string_package_names
from ..api.console import meta, info, success
from subprocess import CalledProcessError

def print_fetching(packages):
    if packages:
        print('🐶  Fetching packages')
    else:
        print('🐶  No packages to fetch!')

def print_fetching_success(packages):
    if packages:
        print('🎾  Successfully installed packages ({})'.format(
            meta(packages)))

def render_line(line, obj):

    action = obj.get('action')
    packages = obj.get('packages', [])
    ext = obj.get('ext')
    url = obj.get('url', {})

    primary_package = packages[0] if packages else {}

    def package_to_string(package):
        name = package.get('name')
        version = package.get('version')
        return '{}'.format((name or '').lower(), version)

    if action == ACTION_COLLECTING:
        if url:
            return info('Collecting {url} ({svc})'.format(
                svc=url.get('svc'),
                url=url.get('url')
            ))
        return info('Collecting {}'.format(primary_package.get('name')))
    elif action == ACTION_CLONING:
        return info('Cloning {}'.format(url.get('url')))
    elif action == ACTION_REQUIREMENT_PREEXISTS:
        dependency_chain = None
        if ext:
            dependency_chain = ' ({})'.format(
                '->'.join([package_to_string(dep) for dep in ext]))
        return success("Requirement '{package}' already satisfied: {dependencies}".format(
            package=package_to_string(primary_package),
            dependencies=(dependency_chain or '')
        ))
    elif action == ACTION_UNINSTALLING:
        return info('Uninstalling {}'.format(primary_package.get('name')))
    else:
        return info(line)

def install_packages(packages):

    default_packages = []
    managed_packages = []

    managed_to_default_map = {}
    resolved_packages = []

    svc_symbols = ['git+', 'hg+', 'bzr+', 'svn+']

    # split packages into default and managed (git+, etc.)
    for package in packages:
        is_managed = False
        for symbol in svc_symbols:
            if package.startswith(symbol):
                is_managed = True
                managed_packages.append(package)
                break
        if not is_managed:
            default_packages.append(package)

    # add default packages to resolved
    resolved_packages.extend(default_packages)

    # install all default packages through pip
    packages_string = string_package_names(default_packages)
    print_fetching(packages_string)

    try:
        for line in io.shell('pip install {}'.format(packages_string)):

            if type(line) is CalledProcessError:
                print(vars(line))
                raise line

            res = parse_line(line)
            action = res.get('action')
            if action:
                print(render_line(line, res))

        # install all managed packages
        for package in managed_packages:
            _package = None
            for line in io.shell('pip install {}'.format(package)):
                res = parse_line(line)
                action = res.get('action')
                if action:
                    if action == ACTION_INSTALLING_SUCCESS:
                        _package = res.get('packages')[0]
                    elif action == ACTION_REQUIREMENT_PREEXISTS:
                        _package = res.get('packages')[1]

                    print(render_line(line, res))

            if _package:
                name = _package.get('name', '').lower()
                managed_to_default_map[name] = package
                resolved_packages.append(name)

    except CalledProcessError as e:
        out = ''
        print(e.output.readlines())
        for line in e.output.readlines():
            out = out + line + '\n'
        raise Exception(
            ('Failed to install.\n' + out))

    print_fetching_success(string_package_names([
        parse_package(package).get('name') for package in resolved_packages]))

    return {
        'packages': resolved_packages,
        'sources': managed_to_default_map
    }

def install_targets(args):

    config = puppy.read()
    packages = format_package_names(args.target)

    res = install_packages(packages)
    resolved_packages = res.get('packages')
    sources = res.get('sources')

    if args.save:
        # add versions to pupfile after installations
        if not puppy.test():
            return

        # get all package versions from pip freeze

        all_packages = {}
        for package in pip.get_packages():
            all_packages[package.get('name', '').lower()] = package

        # update pupfile dependencies with installed packages versions
        for package_name in resolved_packages:

            package = config['dependencies'].get(package_name, {})
            package['version'] = all_packages.get(package_name, {}).get('version')

            source = sources.get(package_name)
            if source:
                package['source'] = source

            config['dependencies'][package_name] = package

        puppy.write(config)


def install_all(args):

    if not puppy.test():
        return

    config = puppy.read()
    dependencies = config.get('dependencies', {})

    packages = []
    for package_name in dependencies:

        package = dependencies.get(package_name)

        name = package_name
        version = package.get('version')
        source = package.get('source')

        if source:
            packages.append(source)
        else:
            packages.append('{}=={}'.format(name, version))

    install_packages(packages)


def cmd_install(args):

    # output the status of the virtual environment
    if venv.exists():
        print('🏠  Using existing virtual environment')
    else:
        print('🏠  Creating new virtual environment')

    # ensure the virtual environment exists
    venv.init()

    # install the packages
    if args.target:
        install_targets(args)
    else:
        install_all(args)
