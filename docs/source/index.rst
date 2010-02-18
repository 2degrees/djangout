Buildout recipes for Django
===========================

:Sponsored by: `2degrees Limited <http://dev.2degreesnetwork.com/>`_.
:Latest release: |release|

.. topic:: Overview

    **Djangout** implements some `Buildout <http://www.buildout.org/>`_
    recipes for `Django <http://www.djangoproject.com/>`_.

The recipes
===========

*admin_media*: Load the absolute path to the media files in Django Admin
------------------------------------------------------------------------

The *admin_media* recipe loads the absolute path to the media files in Django Admin
into a Buildout part, so you can refer to this path from other recipes (i.e.,
in order to let the Web server serve those static files).

This recipe doesn't take any option, so you can just use the following:

.. code-block:: ini

    [buildout]
    parts = django_admin
    
    [django_admin]
    recipe = djangout:admin_media

And the path to this directory will be available from any part/recipe as
``${django_admin:admin_media_root}``.


Example
~~~~~~~

You can use this variable to generate an Apache virtual host configuration from
a template like the one below:

.. code-block:: apache

    <VirtualHost 127.0.0.1:80>
      # ...
      
      Alias /admin_media ${django_admin:admin_media_root}
      
      <Directory ${django_admin:admin_media_root}>
        Order deny,allow
        Allow from all
      </Directory>
      
      # ...
    </VirtualHost>


Links
=====

- `Online documentation <http://packages.python.org/djangout/>`_.
- `Support mailing list <http://groups.google.com/group/2degrees-dev/>`_.
- `Ohloh entry <https://www.ohloh.net/p/djangout>`_ -- Vote for it if you
  use it and find it useful!
- `Development Web site <http://bitbucket.org/2degrees/djangout/>`_:
  The place to report bugs, request features and get the source code.


More information
================

.. toctree::
   :maxdepth: 2
   
   changelog
