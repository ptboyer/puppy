
from unittest import TestCase
from ..api import piputil

class test_piputil(TestCase):

    def test_get_name_version(self):

        line = 'Requirement already satisfied (use --upgrade to upgrade): Flask-SQLAlchemy===3.0.dev0-20170527 from git+http://github.com/user/flask-sqlalchemy.git in ./.puppy/lib/python3.5/site-packages'
        res = piputil.get_name_version(line)
        self.assertEqual(res, {
            'name': 'Flask-SQLAlchemy',
            'version': '3.0.dev0-20170527'
        })

        line = 'Requirement already satisfied: Flask>=0.10 in ./.puppy/lib/python3.5/site-packages (from Flask-SQLAlchemy===3.0.dev0-20170527)'
        res = piputil.get_name_version(line)
        self.assertEqual(res, {
            'name': 'Flask',
            'version': '0.10'
        })

        line = 'Requirement already satisfied: MarkupSafe>=0.23 in ./.puppy/lib/python3.5/site-packages (from Jinja2>=2.4->Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170527)'
        res = piputil.get_name_version(line)
        self.assertEqual(res, {
            'name': 'MarkupSafe',
            'version': '0.23'
        })

        line = 'Cloning http://github.com/user/flask-sqlalchemy.git to /private/var/folders/74/412h5gzx7fdfpp430g8q1nfh0000gn/T/pip-k8pt8307-build'
        res = piputil.get_name_version(line)
        self.assertEqual(res, {
            'name': None,
            'version': None
        })
