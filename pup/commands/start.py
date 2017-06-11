
from ..api import venv, puppy

@venv.required
@puppy.required
def cmd_start(args):

    config = puppy.read()

    target = config.get('main')
    if not target:
        raise Exception("No target specified for 'main' in package file.")

    return python(target)
