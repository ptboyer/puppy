
import os
from termcolor import colored
from ..api.pupfile import read_pupfile, write_pupfile, check_pupfile
from ..api.console import meta
from ..api.constants import PUPFILE_NAME

def req(field, default=''):
    mark = colored('?', 'green')
    field = colored(field, attrs=['bold'])
    _default = '({}) '.format(meta(default)) if default else ''
    return input('{} {}: {}'.format(mark, field, _default)) or default

def cmd_init(args):

    config = read_pupfile()
    config_status = check_pupfile()

    if config_status:
        raise Exception('Package file ({}) already exists. '.format(
            PUPFILE_NAME))

    try:
        # print('This utility will help you create a {} file.'.format(PUPFILE_NAME))
        # print('It tries to guess sensible configuration defaults.')
        # print('Use `pup install <package> --save` to save installed packages.')
        # print('Press ^C at any time to quit.')
        # print('')

        default_name = ''.join(os.getcwd().split('/')[-1:])
        config['name'] = req('name', default_name)

        config['version'] = req('version', '1.0.0')
        config['description'] = req('description')
        config['author'] = req('author')

        config['main'] = req('entry point', 'run.py')
        test = req('test command')
        config['scripts'] = {
            'test': test if test else
            "python -c \"print('no test specified') and exit(1)\""
        }

        keywords = req('keywords')
        config['keywords'] = keywords.split(' ') if keywords else []

        config['license'] = req('license', 'MIT')

        config['dependencies'] = {}

    except KeyboardInterrupt:
        print('')

    else:
        write_pupfile(config)
        print('OK')
