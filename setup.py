# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='ascii-game',
    version='0.0.2',
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
            'ascii-game=ascii_game.ascii_game:cli',
        ]
    }, 
    include_package_data=True,
    zip_safe=False)
