#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="click-aliases",
    version="1.0.7",
    description="Enable aliases for Click",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Robbin Bonthond",
    author_email="robbin@bonthond.com",
    url="https://github.com/click-contrib/click-aliases",
    license="MIT",
    packages=["click_aliases"],
    install_requires=[
        "click",
        "importlib-metadata>=1,<7; python_version<'3.8'",
    ],
    python_requires=">=3.7",
    extras_require={
        "dev": [
            "flake8",
            "flake8-import-order",
            "tox-travis",
            "pytest",
            "pytest-cov",
            "coveralls",
            "wheel",
        ]
    },
)
