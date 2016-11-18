#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
    'gnomic',
    'potion-client'
]

test_requirements = [
    # TODO: put package requirements here
]

setup(
    name='camilo',
    version='0.0.1',
    description="camilo provides functionality to adjust models based on genotypic definitions and phenotypic data available in an iloop instance",
    long_description=readme + '\n\n' + history,
    author="Svetlana Galkina",
    author_email='svegal@biosustain.dtu.dk',
    url='https://github.com/dd-decaf/camilo',
    packages=[
        'camilo',
    ],
    package_dir={'camilo':
                     'camilo'},
    include_package_data=True,
    dependency_links=['https://github.com/biosustain/driven/tarball/master#egg=driven-0.0.4'],
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='camilo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
