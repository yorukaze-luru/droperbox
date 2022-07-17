from setuptools import setup, find_packages
import droperbox

install_requires = [
    'dropbox',
]

setup(
    name='droperbox',
    version=droperbox.__version__,
    packages=find_packages(),
    install_requires=install_requires
)
