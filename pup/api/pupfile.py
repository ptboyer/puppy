
import json
from collections import OrderedDict
from .constants import PUPFILE_NAME
from .console import warn, meta

def read_pupfile():
    data = OrderedDict({})

    try:
        with open(PUPFILE_NAME, 'r') as f:
            data = json.load(f, object_pairs_hook=OrderedDict)
    except:
        pass

    return data

def write_pupfile(data):
    with open(PUPFILE_NAME, 'w') as f:
        json.dump(data, f, indent=2)

def check_pupfile():
    try:
        open(PUPFILE_NAME, 'r')
    except:
        return False
    else:
        return True

def test_pupfile():
    if not check_pupfile():
        print(warn('Package file does not exist! ({})'.format(
            meta(PUPFILE_NAME))))
        return False
    return True

def raise_pupfile_error():
    raise Exception((
        'Package file does not exist! ({})'
        '\n  Use `pup init` to create one.').format(
            meta(PUPFILE_NAME)))

def requires_pupfile(f):
    def wrapper(*args, **kwargs):
        if not check_pupfile():
            raise_pupfile_error()
        return f(*args, **kwargs)
    return wrapper
