
from ..api.venv import requires_venv, python
from ..api.pupfile import read_pupfile, requires_pupfile

@requires_venv
@requires_pupfile
def cmd_start(args):

    config = read_pupfile()
    return python(config.get('main'))
