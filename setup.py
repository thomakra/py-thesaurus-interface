#-------------------------------------------------------------------------------
# Name:     Python Thesaurus Interface
# Purpose:  Python interface to various metadata vocabularies
#
# Author:   Morten Wergeland Hansen, Anton A. Korosov, Aleksander Vines
# Modified: 22.02.2016
#
# Created:  07.12.2015
# Copyright:(c) NERSC
# License:  GPLv3
#-------------------------------------------------------------------------------
from setuptools import setup, find_packages
from os import path

from pythesint import update_vocabulary

here = path.abspath(path.dirname(__file__))
readme_file = 'README.md'
install_requires = ['PyYAML']
NAME = 'pythesint'

# Get the long description from the README file
long_description = ''
if path.exists(path.join(here, readme_file)):
    long_description = open(path.join(here, readme_file)).read()

# fetch all vocabularies from internet
update_vocabulary('gcmd_instruments')
update_vocabulary('gcmd_platforms')
update_vocabulary('gcmd_science_keywords')
update_vocabulary('gcmd_data_centers')
update_vocabulary('gcmd_locations')
update_vocabulary('cf_standard_names')
update_vocabulary('wkv_variables')


setup(
    name=NAME,

    version='1.0.1',

    description='A Python interface to various metadata vocabularies',
    long_description=long_description,

    zip_safe=False,

    author=('Morten W. Hansen', 'Anton A. Korosov', 'Aleksander Vines',),

    author_email='morten.hansen@nersc.no',

    url='https://github.com/nansencenter/py-thesaurus-interface',

    download_url='https://github.com/nansencenter/py-thesaurus-interface/archive/v1.0.0.tar.gz',

    packages=find_packages(),

    install_requires=install_requires,

    test_suite='tests',

    license='GPLv3',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities',
    ],

    keywords='metadata standards thesaurus vocabulary',
)

