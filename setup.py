#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="py-trello",
    version="0.17.0",

    description='Python wrapper around the Trello API',
    long_description=open('README.rst').read(),
    author='Richard Kolkovich',
    author_email='richard@sigil.org',
    url='https://trello.com/board/py-trello/4f145d87b2f9f15d6d027b53',
    download_url='https://github.com/sarumont/py-trello',
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
