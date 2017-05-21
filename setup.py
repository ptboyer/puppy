# -*- coding: utf-8 -*-

from setuptools import setup

__version__ = '0.0.1'

with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')

setup(
    name='puppy-cli',
    packages=[
        'pup',
        'pup.api',
        'pup.commands'
    ],
    entry_points={
        'console_scripts': ['pup=pup.pup:main']
    },
    version=__version__,
    description='Neatly manage your python virtual environments and packages.',
    long_description=long_descr,
    author='Peter Boyer',
    author_email='petertboyer@gmail.com',
    url='https://github.com/ptboyer/puppy',
    install_requires=[
        'virtualenv',
        'termcolor',
    ],
)
