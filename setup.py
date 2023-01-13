from setuptools import setup, Extension, find_packages
import droperbox

VERSION = droperbox.__version__

def _requires_from_file(filename):
    return open(filename).read().splitlines()

packages = [
    'droperbox',
]

setup(
    name='droperbox',
    version=VERSION,
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
)
