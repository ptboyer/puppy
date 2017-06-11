
from termcolor import colored

def success(message):
    head = colored(' OK ', 'green')
    return ('{} {}'.format(head, message))

def warn(message):
    head = colored('WARN', 'yellow')
    return ('{} {}'.format(head, message))

def error(message):
    head = colored('ERR!', 'red')
    return ('{} {}'.format(head, message))

def meta(string):
    return colored(string, 'blue')

def info(message):
    head = colored('INFO', 'white')
    return ('{} {}'.format(head, message))
