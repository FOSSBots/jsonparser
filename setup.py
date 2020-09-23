
from __future__ import print_function
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = [req for req in requirements_file.readlines()]


setup(
    name='jsonparser',
    version='1.0.0',
    description='jsonparser utility for MirahezeBots',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',  # This is important!
    author='MirahezeBot Contributors',
    author_email='bots@miraheze.org',
    url='https://github.com/MirahezeBots/jsonparser',
    include_package_data=True,
    install_requires=requirements,
    license='Eiffel Forum License, version 2',
)
