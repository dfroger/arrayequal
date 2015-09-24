from setuptools import setup

setup(
    name = 'arrayequal',
    version = '0.0.4',
    description = 'test for numpy array equality with unittest support',
    author= 'David Froger',
    author_email = 'david.froger@inria.fr',
    url = '',
    packages = ['arrayequal',],
    install_requires = ['numpy', 'matplotlib', 'Jinja2', 'nose']
    provides = ['arrayequal (0.0.4)'],
)
