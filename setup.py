from setuptools import setup

setup(
    name = 'arrayequal',
    description = 'test for numpy array equality with unittest support',
    author= 'David Froger',
    author_email = 'david.froger@inria.fr',
    url = '',
    packages = ['arrayequal',],
    install_requires = 'numpy',
    provides = ['arrayequal (0.0.1)'],
)
