
from termcolor import colored

def warn(message):
    head = colored('WARN', 'yellow')
    return ('{} {}'.format(head, message))

def error(message):
    head = colored('ERR!', 'red')
    return ('{} {}'.format(head, message))

def meta(string):
    return colored(string, 'blue')
