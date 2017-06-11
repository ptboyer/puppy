
import os
from termcolor import colored
from ..api import puppy
from ..api.console import meta
from ..api.constants import PUPFILE_NAME

def req(field, default=''):
    mark = colored('?', 'green')
    field = colored(field, attrs=['bold'])
    _default = '({}) '.format(meta(default)) if default else ''
    return input('{} {}: {}'.format(mark, field, _default)) or default

def cmd_init(args):

    config = puppy.read()
    config_status = puppy.check()

    if config_status:
        raise Exception('Package file ({}) already exists. '.format(
            PUPFILE_NAME))

    try:
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
        puppy.write(config)
        print('OK')
