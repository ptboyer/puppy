
from unittest import TestCase
from ..api import venv

class test_venv(TestCase):

    def test_virtualise(self):

        res = venv.virtualise('python run.py', 'python')
        self.assertEqual(res, '.puppy/bin/python run.py')

        res = venv.virtualise('pip install package', 'pip')
        self.assertEqual(res, '.puppy/bin/pip install package')

        res = venv.virtualise('/usr/bin/yes | pip install package', 'pip')
        self.assertEqual(res, '/usr/bin/yes | .puppy/bin/pip install package')
