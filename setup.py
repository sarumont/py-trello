#!/usr/bin/env python

import os
from setuptools import setup, find_packages


ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as _file:
    long_description = _file.read()

setup(
    name = "py-trello",
    version = "0.1",

    description='wrapper around the Trello API',
    long_description=long_description,
    author='Richard Kolkovich',
    url='https://trello.com/board/py-trello/4f145d87b2f9f15d6d027b53',
    keywords='python',
    license='BSD License',
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires= ['httplib2', ],
    packages = find_packages(),
    include_package_data=True,
)
