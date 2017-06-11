
import json
from collections import OrderedDict
from .constants import PUPFILE_NAME
from .console import warn, meta

def read():
    data = OrderedDict({})

    try:
        with open(PUPFILE_NAME, 'r') as f:
            data = json.load(f, object_pairs_hook=OrderedDict)
    except:
        pass

    return data

def write(data):
    with open(PUPFILE_NAME, 'w') as f:
        json.dump(data, f, indent=2)

def check():
    try:
        open(PUPFILE_NAME, 'r')
    except:
        return False
    else:
        return True

def test():
    if not check():
        print(warn('Package file does not exist! ({})'.format(
            meta(PUPFILE_NAME))))
        return False
    return True

def raise_error():
    raise Exception((
        'Package file does not exist! ({})'
        '\n  Use `pup init` to create one.').format(
            meta(PUPFILE_NAME)))

def required(f):
    def wrapper(*args, **kwargs):
        if not check():
            raise_error()
        return f(*args, **kwargs)
    return wrapper
