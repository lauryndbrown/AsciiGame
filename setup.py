# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='ASCII Game',
    version='0.0.1',
    description='Terminal-Based Game Framework',
    url='https://github.com/lauryndbrown/AsciiGame',
    author='Lauryn Brown',
    author_email='lauryndbrown@gmail.com',
    license='GNU GPLv3',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'Click',
    ],
    entry_points={
        'console_scripts':[
            'ascii_game=ascii_game.ascii_game:cli',
        ]
    }, 
    include_package_data=True,
    zip_safe=False)
