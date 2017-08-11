
test_shell_read_clean = [
    "Collecting git+http://github.com/nickw444/flask-sqlalchemy.git",
    "Cloning http://github.com/nickw444/flask-sqlalchemy.git to /private/var/folders/74/412h5gzx7fdfpp430g8q1nfh0000gn/T/pip-17i78c85-build",
    "Collecting Flask>=0.10 (from Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached Flask-0.12.2-py2.py3-none-any.whl",
    "Collecting SQLAlchemy>=0.8.0 (from Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Collecting Werkzeug>=0.7 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached Werkzeug-0.12.2-py2.py3-none-any.whl",
    "Collecting itsdangerous>=0.21 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Collecting Jinja2>=2.4 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached Jinja2-2.9.6-py2.py3-none-any.whl",
    "Collecting click>=2.0 (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Using cached click-6.7-py2.py3-none-any.whl",
    "Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170609)",
    "Installing collected packages: Werkzeug, itsdangerous, MarkupSafe, Jinja2, click, Flask, SQLAlchemy, Flask-SQLAlchemy",
    "Running setup.py install for Flask-SQLAlchemy: started",
    "Running setup.py install for Flask-SQLAlchemy: finished with status 'done'",
    "Successfully installed Flask-0.12.2 Flask-SQLAlchemy-3.0.dev0-20170609 Jinja2-2.9.6 MarkupSafe-1.0 SQLAlchemy-1.1.10 Werkzeug-0.12.2 click-6.7 itsdangerous-0.24",
]

test_shell_read_dirty = [
    "Collecting git+http://github.com/nickw444/flask-sqlalchemy.git",
    "Cloning http://github.com/nickw444/flask-sqlalchemy.git to /private/var/folders/74/412h5gzx7fdfpp430g8q1nfh0000gn/T/pip-x9p055zu-build",
    "Requirement already satisfied: Flask>=0.10 in ./.puppy/lib/python3.5/site-packages (from Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: SQLAlchemy>=0.8.0 in ./.puppy/lib/python3.5/site-packages (from Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: Jinja2>=2.4 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: itsdangerous>=0.21 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: Werkzeug>=0.7 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: click>=2.0 in ./.puppy/lib/python3.5/site-packages (from Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Requirement already satisfied: MarkupSafe>=0.23 in ./.puppy/lib/python3.5/site-packages (from Jinja2>=2.4->Flask>=0.10->Flask-SQLAlchemy===3.0.dev0-20170608)",
    "Installing collected packages: Flask-SQLAlchemy",
    "Found existing installation: Flask-SQLAlchemy 3.0.dev0-20170607",
    "Uninstalling Flask-SQLAlchemy-3.0.dev0-20170607:",
    "Successfully uninstalled Flask-SQLAlchemy-3.0.dev0-20170607",
    "Running setup.py install for Flask-SQLAlchemy: started",
    "Running setup.py install for Flask-SQLAlchemy: finished with status 'done'",
    "Successfully installed Flask-SQLAlchemy-3.0.dev0-20170608",
]

test_shell_read_noent = [
    "Collecting jumpstart-xxx",
    "Could not find a version that satisfies the requirement jumpstart-xxx (from versions: )",
    "No matching distribution found for jumpstart-xxx",
]

test_shell_no_match_dist = [
    "Collecting flask==45.13.1",
    "Could not find a version that satisfies the requirement flask==45.13.1 (from versions: 0.1, 0.2, 0.3, 0.3.1, 0.4, 0.5, 0.5.1, 0.5.2, 0.6, 0.6.1, 0.7, 0.7.1, 0.7.2, 0.8, 0.8.1, 0.9, 0.10, 0.10.1, 0.11, 0.11.1, 0.12, 0.12.1, 0.12.2)",
    "No matching distribution found for flask==45.13.1",
]
