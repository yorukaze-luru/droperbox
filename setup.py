from setuptools import setup, Extension, find_packages
import droperbox

VERSION = droperbox.__version__

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
    version=VERSION,
    packages=find_packages(),
    install_requires=load_requires_from_file('requirements.txt'),
    include_package_data=True,
)
