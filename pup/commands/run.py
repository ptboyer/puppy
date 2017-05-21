
from ..api.venv import requires_venv, python, script
from ..api.pupfile import (
    read_pupfile, check_pupfile,
    test_pupfile, raise_pupfile_error)

@requires_venv
def cmd_run(args):

    config = read_pupfile()

    target = args.target
    if not target:
        return python()

    # only concern the first arg
    if target[0].endswith('.py'):
        test_pupfile()
        return python(' '.join(args.target))

    # scripts require a pupfile
    if not check_pupfile():
        return raise_pupfile_error()

    target_script = config.get('scripts', {}).get(target)
    if target_script:
        return script(target_script)

    raise Exception('Script ({}) not found.'.format(target))
