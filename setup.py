# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cvp-sanity',
    version='0.1',
    description='set of tests for MCP verification',
    long_description=readme,
    author='Mirantis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
