#!/usr/bin/env python

from setuptools import setup

setup(
    name='neo4j_rest_client',
    version='0.1',
    author='Javier de la Rosa',
    url='https://github.com/versae/neo4j-rest-client',
    packages=['neo4j_rest_client'],
    install_requires=[
        'httplib2',
    ]
)