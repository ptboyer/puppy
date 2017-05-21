
from ..api.venv import requires_venv, python, script
from ..api.pupfile import read_pupfile, requires_pupfile

@requires_venv
@requires_pupfile
def cmd_run(args):

    config = read_pupfile()

    target = args.target
    if not target:
        return python()

    # only concern the first arg
    target = target[0]

    target_script = config.get('scripts', {}).get(target)
    if target_script:
        return script(target_script)

    raise Exception('Script ({}) not found.'.format(target))
