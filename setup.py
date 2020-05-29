import os
from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'spine',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev0')

setup(
    name='spine',
    version=version,
    description='SPINE is a simple Spiking Neuron simulator',
    long_description='README.md',
    author='Hiroshi ARAKI',
    author_email='araki@hirlab.net',
    install_requires=read_requirements(),
    url='https://github.com/HiroshiARAKI/spine',
    license='MIT',
    packages=find_packages(exclude=('img',)),
    test_suite='tests',
)
