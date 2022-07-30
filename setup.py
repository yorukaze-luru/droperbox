from setuptools import setup, Extension, find_packages
import droperbox

VERSION = droperbox.__version__

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='droperbox',
    version=VERSION,
    packages=find_packages(where='droperbox'),
    package_dir={'': 'droperbox'},
    install_requires=_requires_from_file('requirements.txt'),
)
