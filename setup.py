from setuptools import setup, find_packages

install_requires = [
    'dropbox'
]

setup(
    name='droperbox',
    version='0.0.2',
    packages=find_packages(),
    install_requires=install_requires
)
