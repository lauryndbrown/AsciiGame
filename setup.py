# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
#License not yet added
#with open('LICENSE') as f:
#    license = f.read()
setup(
    name='sample',
    version='0.0.1',
    description='Terminal-Based Game Framework',
    long_description=readme,
    author='Lauryn Brown',
    author_email='',
    url='github',
    license='license',
    packages=find_packages(exclude=('tests', 'docs'))
)
