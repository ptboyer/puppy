
import shutil
from ..api.venv import requires_venv
from ..api.constants import VENV_NAME, VENV_PATH
from ..api.console import meta

@requires_venv
def cmd_destroy(args):

    print('🔥  Destroying virtual environment ({})'.format(
        meta(VENV_NAME)))

    shutil.rmtree(VENV_PATH)
