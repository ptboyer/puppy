# -*- coding: utf-8 -*-

import argparse

from .commands import (
    cmd_init,
    cmd_install,
    cmd_uninstall,
    cmd_list,
    cmd_start,
    cmd_run,
    cmd_destroy
)

from .api.console import error

__version__ = '0.0.1'

def main():

    parser = argparse.ArgumentParser(
        description='PUP Uncomplicates Packages')
    parser.add_argument(
        'command', metavar='command', type=str)
    parser.add_argument(
        'target', metavar='target', nargs='*', type=str)
    parser.add_argument(
        '--save', action='store_true', required=False)

    args = parser.parse_args()

    commands = {
        'init': cmd_init,
        'install': cmd_install,
        'uninstall': cmd_uninstall,
        'list': cmd_list,
        'start': cmd_start,
        'run': cmd_run,
        'destroy': cmd_destroy
    }

    try:
        if not commands.get(args.command):
            raise Exception('Not a valid command.')

        commands[args.command](args)

    except Exception as e:
        if (str(e).find('Failed to establish a new connection') != -1):
            e = 'Failed to establish network connection.'
        print(error(e))
        # raise(e)
        return exit(1)

    else:
        return exit(0)
