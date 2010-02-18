# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2010, 2degrees Limited.
# All Rights Reserved.
#
# This file is part of Djangout: <http://bitbucket.org/2degrees/djangout>.
#
# Djangout is subject to the provisions of the BSD license that accompanies
# that distribution. An incomplete copy of that text is also available at
# <http://dev.2degreesnetwork.com/p/2degrees-license.html>. THIS SOFTWARE IS
# PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF TITLE,
# MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
#
################################################################################
import os

# Setuptools is obviously available, so there's no need to use ez_setup:
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGELOG = open(os.path.join(here, "docs", "source", "changelog.rst")).read()
version = open(os.path.join(here, "VERSION.txt")).readline().rstrip()

setup(name="djangout",
      version=version,
      description="Buildout recipes for Django",
      long_description="\n".join((README, CHANGELOG)),
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Buildout",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP",
        ],
      keywords="buildout recipe django media",
      author="2degrees Limited",
      author_email="2degrees-dev@googlegroups.com",
      url="http://bitbucket.org/2degrees/djangout/",
      license="BSD (http://dev.2degreesnetwork.com/p/2degrees-license.html)",
      py_modules=["djangout"],
      package_data={
        '': ["VERSION.txt", "README.txt"],
        'docs': ["Makefile", "source/*"],
        },
      exclude_package_data={"": ["README.txt", "docs"]},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "zc.buildout >= 1.4.0",
        "zc.recipe.egg >= 1.1.0",
        "Django >= 1.0",
        ],
      entry_points = """\
        [zc.buildout]
        admin_media = djangout:AdminMediaRecipe
      """
      )
