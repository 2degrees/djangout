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
"""
Buildout recipes for Buildout.

"""
from os import path
from logging import getLogger

from pkg_resources import working_set
from zc.recipe.egg import Eggs

_LOGGER = getLogger(__name__)


class AdminMediaRecipe(object):
    """
    Recipe to make available the path to the media files in Django Admin.
    
    """
    
    def __init__(self, buildout, name, options):
        if "eggs" not in options:
            # If we don't set the "eggs" option, it will take the part name:
            options['eggs'] = ""
            _LOGGER.debug("Set the 'eggs' option to an empty string")
        ws = Eggs(buildout, name, options).working_set(["django >= 1.0"])[1]
        for dist in ws:
            working_set.add(dist)
        
        # Finding the path to the media in Django Admin:
        from django import __file__ as django_file
        django_root = path.dirname(django_file)
        admin_media = path.join(django_root, "contrib", "admin", "media")
        # We found it, let's make it available to other recipes/parts:
        options['admin_media_root'] = admin_media
    
    def install(self):
        return ()
    
    def update(self):
        return ()
