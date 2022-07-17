from setuptools import setup, find_packages
import droperbox

VERSION = droperbox.__version__

install_requires = [
    'dropbox',
]

setup(
    name='droperbox',
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requires
)
