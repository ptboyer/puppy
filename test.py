test_shell_read_clean = [
    "Collecting git+http://github.com/nickw444/flask-sqlalchemy.git",
    "Cloning http://github.com/nickw444/flask-sqlalchemy.git to /private/var/folders/74/412h5gzx7fdfpp430g8q1nfh0000gn/T/pip-17i78c85-build",
    "Collecting Flask>=0.10 (from Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached Flask-0.12.2-py2.py3-none-any.whl",
    "Collecting SQLAlchemy>=0.8.0 (from Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Collecting Werkzeug>=0.7 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached Werkzeug-0.12.2-py2.py3-none-any.whl",
    "Collecting itsdangerous>=0.21 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Collecting Jinja2>=2.4 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached Jinja2-2.9.6-py2.py3-none-any.whl",
    "Collecting click>=2.0 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached click-6.7-py2.py3-none-any.whl",
    "Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Installing collected packages: Werkzeug, itsdangerous, MarkupSafe, Jinja2, click, Flask, SQLAlchemy, Flask-SQLAlchemy",
    "Running setup.py install for Flask-SQLAlchemy: started",
    "Running setup.py install for Flask-SQLAlchemy: finished with status 'done'",
    "Successfully installed Flask-0.12.2 Flask-SQLAlchemy-3.0.dev0-20170609 Jinja2-2.9.6 MarkupSafe-1.0 SQLAlchemy-1.1.10 Werkzeug-0.12.2 click-6.7 itsdangerous-0.24",
]

test_shell_read_dirty = [
    "Collecting git+http://github.com/nickw444/flask-sqlalchemy.git",
    "Cloning http://github.com/nickw444/flask-sqlalchemy.git to /private/var/folders/74/412h5gzx7fdfpp430g8q1nfh0000gn/T/pip-x9p055zu-build",
    "Requirement already satisfied: Flask>=0.10 in ./.puppy/lib/python3.5/site-packages (from Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: SQLAlchemy>=0.8.0 in ./.puppy/lib/python3.5/site-packages (from Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: Jinja2>=2.4 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: itsdangerous>=0.21 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: Werkzeug>=0.7 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: click>=2.0 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: MarkupSafe>=0.23 in ./.puppy/lib/python3.5/site-packages (from Jinja2>=2.4->Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Installing collected packages: Flask-SQLAlchemy",
    "Found existing installation: Flask-SQLAlchemy 3.0.dev0-20170607",
    "Uninstalling Flask-SQLAlchemy-3.0.dev0-20170607:",
    "Successfully uninstalled Flask-SQLAlchemy-3.0.dev0-20170607",
    "Running setup.py install for Flask-SQLAlchemy: started",
    "Running setup.py install for Flask-SQLAlchemy: finished with status 'done'",
    "Successfully installed Flask-SQLAlchemy-3.0.dev0-20170608",
]

test_shell_read_noent = [
    "Collecting jumpstart-xxx",
    "Could not find a version that satisfies the requirement jumpstart-xxx (from versions: )",
    "No matching distribution found for jumpstart-xxx",
]

test_shell_no_match_dist = [
    "Collecting flask==45.13.1",
    "Could not find a version that satisfies the requirement flask==45.13.1 (from versions: 0.1, 0.2, 0.3, 0.3.1, 0.4, 0.5, 0.5.1, 0.5.2, 0.6, 0.6.1, 0.7, 0.7.1, 0.7.2, 0.8, 0.8.1, 0.9, 0.10, 0.10.1, 0.11, 0.11.1, 0.12, 0.12.1, 0.12.2)",
    "No matching distribution found for flask==45.13.1",
]

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


def get_line_action(line):
    if line.startswith(LS_COLLECTING_PREFIX):
        return ACTION_COLLECTING
    elif line.startswith(LS_CLONING_PREFIX):
        return ACTION_CLONING
    elif line.startswith(LS_USING_CACHED_PREFIX):
        return ACTION_USING_CACHED
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


def get_line_url(line, action=None):

    if not action:
        action = get_line_action(line)

    def parse_url(url):
        if 'http://' in url or 'https://' in url:
            if '+' in url:
                _svc, _url = url.split('+')
            else:
                _svc, _url = (None, url,)
            return {'url': _url, 'svc': _svc}
        else:
            return None

    if action == ACTION_COLLECTING:
        url = line[len(LS_COLLECTING_PREFIX):]
        return parse_url(url)
    elif action == ACTION_CLONING:
        url = line[len(LS_CLONING_PREFIX):line.find(' to ')]
        return parse_url(url)

    return None


def get_line_packages(line, action=None):

    if not action:
        action = get_line_action(line)

    def parse_package(package):
        symbols = ['===', '==', '>=', '<=']
        for symbol in symbols:
            if symbol in package:
                _name, _version = package.split(symbol)
                return {'name': _name, 'version': _version}
        return {'name': package, 'version': None}

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
    elif action == ACTION_INSTALLING_STARTED:
        if LS_INSTALLING_STARTED_SUFFIX in line:
            package = line[len(LS_INSTALLING_PREFIX):line.find(LS_INSTALLING_STARTED_SUFFIX)]
            packages.append(parse_package(package))
        elif LS_INSTALLING_SUCCESS_SUFFIX in line:
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


def get_line_ref(line, action=None):

    if not action:
        action = get_line_action(line)

    if action == ACTION_USING_CACHED:
        # string of cached resource name
        return line[len(LS_USING_CACHED_PREFIX):]
    if action == ACTION_NO_VERSION_FOUND:
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
    ref = get_line_ref(line, action)

    return {
        'action': action,
        'packages': packages,
        'url': url,
        'ref': ref
    }

packages = []
for line in test_shell_no_match_dist:
    data = parse_line(line)

    print(line)
    print(data.get('action'), data)
    print('')

    if data.get('packages'):
        packages.extend(data.get('packages'))

# print(packages)
