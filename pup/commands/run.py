
from ..api import venv, puppy

@venv.required
def cmd_run(args):

    config = puppy.read()

    target = args.target
    if not target:
        return python()

    # only concern the first arg
    if target[0].endswith('.py'):
        puppy.test()
        return python(' '.join(args.target))

    # scripts require a pupfile
    if not puppy.check():
        return puppy.raise_error()

    target_script = config.get('scripts', {}).get(target)
    if target_script:
        return script(target_script)

    raise Exception('Script ({}) not found.'.format(target))
