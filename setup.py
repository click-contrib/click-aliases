#!/usr/bin/env python

from setuptools import setup

setup(
    name='click-aliases',
    version='0.1',
    description='Enable aliases for Click',
    author='Robbin Bonthond',
    author_email='robbin@bonthond.com',
    url='https://github.com/rbonthond/click-aliases',
    license='MIT',
    packages=['click_aliases'],
    install_requires=[
        'click',
    ]
)
