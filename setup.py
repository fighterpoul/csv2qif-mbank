#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='csv2qif_mbank',
    version='0.0.1',
    description='Convert CSV from mBank account to QIF file',
    long_description=read("README.md"),
    author='Paweł Walczak',
    author_email='fighter.poul@gmail.com',
    packages=find_packages(exclude=["tests"]),
    python_requires='>3.5',
    license=read("LICENSE")
)
