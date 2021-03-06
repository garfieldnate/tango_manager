#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0', 'asciimatics', 'requests', 'python-dateutil',
]

setup_requirements = [
]

test_requirements = [
]

setup(
    name='tango',
    version='0.1.0',
    description="TUI for studying and managing 単語",
    long_description=readme + '\n\n' + history,
    author="Nathan Glenn",
    author_email='garfieldnate@gmail.com',
    url='https://github.com/garfieldnate/tango',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tango=tango.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords=['education', 'vocabulary', 'spaced repetition'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
