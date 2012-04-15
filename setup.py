#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name = "py-trello",
	version = "0.1",

	description = 'Python wrapper around the Trello API',
	long_description = open('README.md').read(),
	author = 'Richard Kolkovich',
	author_email = 'richard@sigil.org',
	url = 'https://trello.com/board/py-trello/4f145d87b2f9f15d6d027b53',
	keywords = 'python',
	license = 'BSD License',
	classifiers = [
		"Development Status :: 4 - Beta",
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
	],
	install_requires = ['httplib2', ],
	packages = find_packages(),
	include_package_data = True,
)
