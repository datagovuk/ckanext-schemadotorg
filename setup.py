from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-schemadotorg',
    version=version,
    description="Adds schema.org schema to organizations and datasets.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Ross Jones',
    author_email='ross@servercode.co.uk',
    url='https://bitbucket.org/leedsdatamill/ckanext-schemadotorg',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.schemadotorg'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        schemadotorg=ckanext.schemadotorg.plugin:SDOPlugin
    ''',
)
