
ACTION_COLLECTING = 'ACTION_COLLECTING'
ACTION_CLONING = 'ACTION_CLONING'
ACTION_USING_CACHED = 'ACTION_USING_CACHED'
ACTION_INSTALLING_STARTED = 'ACTION_INSTALLING_STARTED'
ACTION_INSTALLING_SUCCESS = 'ACTION_INSTALLING_SUCCESS'
ACTION_INSTALLING_COLLECTED = 'ACTION_INSTALLING_COLLECTED'
ACTION_SUCCESS_ALL = 'ACTION_SUCCESS_ALL'
ACTION_REQUIREMENT_PREEXISTS = 'ACTION_REQUIREMENT_PREEXISTS'
ACTION_NO_VERSION_FOUND = 'ACTION_NO_VERSION_FOUND'
ACTION_NO_DISTRIBUTION_FOUND = 'ACTION_NO_DISTRIBUTION_FOUND'

LS_COLLECTING_PREFIX = 'Collecting '
LS_CLONING_PREFIX = 'Cloning '
LS_USING_CACHED_PREFIX = 'Using cached '
LS_INSTALLING_PREFIX = 'Running setup.py install for '
LS_INSTALLING_STARTED_SUFFIX = ': started'
LS_INSTALLING_SUCCESS_SUFFIX = ': finished with status'
LS_INSTALLING_COLLECTED_PREFIX = 'Installing collected packages: '
LS_SUCCESS_ALL_PREFIX = 'Successfully installed '
LS_REQUIREMENT_PREEXISTS_PREFIX = 'Requirement already satisfied: '
LS_NO_VERSION_FOUND_PREFIX = 'Could not find a version that satisfies the requirement '
LS_NO_VERSION_FOUND_SUFFIX = ' (from versions: '
LS_NO_DISTRIBUTION_FOUND_PREFIX = 'No matching distribution found for '

LS_EGG_PREFIX = '#egg='

def get_line_action(line):

    if line.startswith(LS_COLLECTING_PREFIX):
        return ACTION_COLLECTING
    elif line.startswith(LS_CLONING_PREFIX):
        return ACTION_CLONING
    elif line.startswith(LS_USING_CACHED_PREFIX):
        return ACTION_USING_CACHED
    elif line.startswith(LS_REQUIREMENT_PREEXISTS_PREFIX):
        return ACTION_REQUIREMENT_PREEXISTS
    elif line.startswith(LS_INSTALLING_PREFIX):
        if LS_INSTALLING_STARTED_SUFFIX in line:
            return ACTION_INSTALLING_STARTED
        elif LS_INSTALLING_SUCCESS_SUFFIX in line:
            return ACTION_INSTALLING_SUCCESS
    elif line.startswith(LS_INSTALLING_COLLECTED_PREFIX):
        return ACTION_INSTALLING_COLLECTED
    elif line.startswith(LS_SUCCESS_ALL_PREFIX):
        return ACTION_SUCCESS_ALL
    elif line.startswith(LS_NO_VERSION_FOUND_PREFIX):
        return ACTION_NO_VERSION_FOUND
    elif line.startswith(LS_NO_DISTRIBUTION_FOUND_PREFIX):
        return ACTION_NO_DISTRIBUTION_FOUND


def parse_url(url):
    if 'http://' in url or 'https://' in url:
        if '+' in url:
            _svc, _url = url.split('+')
        else:
            _svc, _url = (None, url,)
        return {'url': _url, 'svc': _svc}
    else:
        return None


def get_line_url(line, action=None):

    if not action:
        action = get_line_action(line)

    if action == ACTION_COLLECTING:
        url = line[len(LS_COLLECTING_PREFIX):]
        return parse_url(url)
    elif action == ACTION_CLONING:
        url = line[len(LS_CLONING_PREFIX):line.find(' to ')]
        return parse_url(url)

    return None


def parse_package(package):
    symbols = ['===', '==', '>=', '<=']
    for symbol in symbols:
        if symbol in package:
            _name, _version = package.split(symbol)
            return {'name': _name, 'version': _version}
    return {'name': package, 'version': None}


def find_from_end(string, substring):
    _string = string[::-1]
    _substring = substring[::-1]
    position = _string.find(_substring)
    if not position == -1:
        position = len(string) - len(substring) - position
    return position


def get_line_packages(line, action=None):

    if not action:
        action = get_line_action(line)

    packages = []

    if action == ACTION_COLLECTING:
        if ' (from ' in line:
            package = line[len(LS_COLLECTING_PREFIX):line.find(' (from ')]
            packages.append(parse_package(package))
        else:
            package = line[len(LS_COLLECTING_PREFIX):]
            packages.append(parse_package(package))
    elif action == ACTION_REQUIREMENT_PREEXISTS:
        package = line[len(LS_REQUIREMENT_PREEXISTS_PREFIX):line.find(' in ')]
        packages.append(parse_package(package))
        delimiter = ' (from '
        if delimiter in line:
            if '->' in line:
                delimiter = '->'
            package = line[find_from_end(line, delimiter) + len(delimiter):-1]
            packages.append(parse_package(package))
    elif action == ACTION_INSTALLING_STARTED:
        package = line[len(LS_INSTALLING_PREFIX):line.find(LS_INSTALLING_STARTED_SUFFIX)]
        packages.append(parse_package(package))
    elif action == ACTION_INSTALLING_SUCCESS:
        package = line[len(LS_INSTALLING_PREFIX):line.find(LS_INSTALLING_SUCCESS_SUFFIX)]
        packages.append(parse_package(package))
    elif action == ACTION_INSTALLING_COLLECTED:
        _packages = line[len(LS_INSTALLING_COLLECTED_PREFIX):].split(' ')
        for _package in _packages:
            packages.append(parse_package(_package))
    elif action == ACTION_SUCCESS_ALL:
        _packages = line[len(LS_SUCCESS_ALL_PREFIX):].split(' ')
        for _package in _packages:
            packages.append(parse_package(_package))
    elif action == ACTION_NO_VERSION_FOUND:
        package = line[len(LS_NO_VERSION_FOUND_PREFIX):line.find(LS_NO_VERSION_FOUND_SUFFIX)]
        packages.append(parse_package(package))
    elif action == ACTION_NO_DISTRIBUTION_FOUND:
        package = line[len(LS_NO_DISTRIBUTION_FOUND_PREFIX):]
        packages.append(parse_package(package))

    return packages


def get_line_ext(line, action=None):

    if not action:
        action = get_line_action(line)

    if action == ACTION_USING_CACHED:
        # string of cached resource name
        return line[len(LS_USING_CACHED_PREFIX):]
    elif action == ACTION_REQUIREMENT_PREEXISTS:
        # array of packages from "from" chain
        delimiter = ' (from '
        if delimiter not in line:
            return []
        chain = line[line.find(delimiter) + len(delimiter):-1]
        packages = []
        for package in chain.split('->'):
            packages.append(parse_package(package))
        return packages

    elif action == ACTION_NO_VERSION_FOUND:
        # array of versions
        versions = line[line.find(LS_NO_VERSION_FOUND_SUFFIX) + len(LS_NO_VERSION_FOUND_SUFFIX):-1]
        versions = versions.split(', ')
        if versions:
            return versions

    return None


def parse_line(line):

    line = line.strip()

    action = get_line_action(line)
    packages = get_line_packages(line, action)
    url = get_line_url(line, action)
    ext = get_line_ext(line, action)

    return {
        'action': action,
        'packages': packages,
        'url': url,
        'ext': ext
    }
