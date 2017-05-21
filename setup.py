# -*- coding: utf-8 -*-

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pup/pup.py').read(),
    re.M
).group(1)

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="puppy-cli",
    packages=["pup"],
    entry_points={
        "console_scripts": ['pup=pup.pup:main']
    },
    version=version,
    description="Neatly manage your python virtual environments and packages.",
    long_description=long_descr,
    author="Peter Boyer",
    author_email="petertboyer@gmail.com",
    url="https://github.com/ptboyer/puppy",
)
