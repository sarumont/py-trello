#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="ha-py-trello",
    version="0.22.0",

    description='Python wrapper around the Trello API (Home Assistant specific)',
    long_description=open('README.md').read(),
    author='Scott Giminiani (originally Richard Kolkovich)',
    author_email='scottg489@gmail.com',
    url='https://github.com/ScottG489/ha-py-trello',
    download_url='https://github.com/ScottG489/ha-py-trello',
    keywords='python',
    license='BSD License',
    classifiers=[
        "Development Status :: 4 - Beta",
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
    ],
    install_requires=["requests", "requests-oauthlib >= 0.4.1", "python-dateutil", "pytz"],
    packages=find_packages(),
    include_package_data=True,
)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
