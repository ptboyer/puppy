
import shutil
from ..api import venv
from ..api.constants import VENV_NAME, VENV_PATH
from ..api.console import meta

@venv.required
def cmd_destroy(args):

    print('🔥  Destroying virtual environment')

    shutil.rmtree(VENV_PATH)
