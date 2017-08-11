
import re
import subprocess
from subprocess import CalledProcessError

def shell_run(command):

    return subprocess.run(
        [command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)

def shell_popen(command):

    popen = subprocess.Popen(
        [command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        shell=True)

    for line in popen.stdout:
        yield line.strip()

    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        yield CalledProcessError(return_code, command, popen.stderr)

def virtualise(command, target, path):
    return re.sub(
        r'\b(%s)\b' % target,
        '{}/{}'.format(path, target),
        command,
        flags=re.IGNORECASE)

class IO(object):

    def __init__(self, path, targets):
        self._path = path or ''
        self._targets = targets or []

    def shell(self, command, sync=False, virtual=True):

        if virtual:
            for target in self._targets:
                command = virtualise(command, target, self._path)

        if sync:
            return shell_run(command)
        else:
            return shell_popen(command)
