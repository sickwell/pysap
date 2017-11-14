#!/usr/bin/env python
# ===========
# pysap - Python library for crafting SAP's network protocols packets
#
# Copyright (C) 2012-2017 by Martin Gallo, Core Security
#
# The library was designed and developed by Martin Gallo from the Security
# Consulting Services team of Core Security.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# ==============

# Standard imports
from sys import exit
from os import system
from setuptools import setup, Extension, Command
# Custom imports
import pysap


class APIDocumentationCommand(Command):
    """Custom command for building the documentation with Sphinx.
    """

    description = "Builds the documentation using Sphinx"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Runs Sphinx
        """
        exit(system("cd docs && make html"))


class PreExecuteNotebooksCommand(Command):
    """Custom command for pre-executing Jupyther notebooks included in the documentation.
    """

    description = "Pre-executes Jupyther notebooks included in the documentation"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Pre executes notebooks
        """
        system("jupyter nbconvert --inplace --to notebook --execute docs/protocols/*.ipynb")
        system("jupyter nbconvert --inplace --to notebook --execute docs/fileformats/*.ipynb")


sapcompress = Extension('pysapcompress',
                        ['pysapcompress/pysapcompress.cpp',
                         'pysapcompress/vpa105CsObjInt.cpp',
                         'pysapcompress/vpa106cslzc.cpp',
                         'pysapcompress/vpa107cslzh.cpp',
                         'pysapcompress/vpa108csulzh.cpp'],
                        define_macros=[  # Enable this macro if you want some debugging information on the (de)compression functions
                                       #('DEBUG', None),
                                         # Enable this macro if you want detailed debugging information (hexdumps) on the (de)compression functions
                                       #('DEBUG_TRACE', None),
                        ])


setup(name=pysap.__title__,   # Package information
      version=pysap.__version__,
      author='Martin Gallo',
      author_email='mgallo@coresecurity.com',
      description='Python library for crafting SAP\'s network protocols packets',
      long_description=pysap.__doc__,  # @UndefinedVariable
      url=pysap.__url__,
      download_url=pysap.__url__,
      license=pysap.__license__,
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Information Technology',
                   'Intended Audience :: System Administrators',
                   'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                   'Programming Language :: Python',
                   'Programming Language :: C++',
                   'Topic :: Security'],
      # Packages list
      packages=['pysap'],
      provides=['pysapcompress', 'pysap'],

      # Extension module compilation
      ext_modules=[sapcompress],

      # Script files
      scripts=['bin/pysapcar'],

      # Tests command
      test_suite='tests.test_suite',

      # Documentation commands
      cmdclass={'doc': APIDocumentationCommand,
                'notebooks': PreExecuteNotebooksCommand},

      # Requirements
      install_requires=open('requirements.txt').read().splitlines(),

      # Optional requirements for docs and some examples
      extras_require={"docs": open('requirements-docs.txt').read().splitlines(),
                      "examples": open('requirements-optional.txt').read().splitlines()},
      )
