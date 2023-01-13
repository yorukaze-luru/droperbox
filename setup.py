from setuptools import setup, Extension, find_packages

VERSION = '2.0.1'

import os

def load_requires_from_file(fname):
    if not os.path.exists(fname):
        raise IOError(fname)
    return [pkg.strip() for pkg in open(fname, 'r')]

packages = [
    'droperbox',
]

setup(
    name='droperbox',
    url="https://github.com/8ka1alu/droperbox",
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requires_from_file('requirements.txt'),
)
