#!/usr/bin/env python
# encoding: utf8

from setuptools import setup, find_packages

setup(
    name='valueobject',
    version='1.0.0',
    description='ValueObject is a dict-like object that exposes keys as attributes.',
    author='Felix Schwarz, Martin Häcker, Robert Buchholz',
    author_email='rbu@goodpoint.de, spamfaenger@gmx.de',
    license='ISC',
    url='https://gitlab.com/rbuchholz/valueobject',
    packages=find_packages(),
    extras_require=dict(
        testing=['PythonicTestcase',],
    ),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
