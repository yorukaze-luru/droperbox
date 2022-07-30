from setuptools import setup, Extension, find_packages
import droperbox

VERSION = droperbox.__version__

requirements = []
with open('requirements.txt') as f:
     requirements = f.read().splitlines()

packages = [
    'droperbox',
]

setup(
    name='droperbox',
    version=VERSION,
    packages=packages
    install_requires=requirements,
)
