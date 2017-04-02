.. _tests:

Tests
*****

`Continuous integration test results <https://travis-ci.org/richardcornish/django-pygmentify>`_ are available online.

However, you can also test the source code.

.. code-block:: bash

   $ workon myvenv
   $ django-admin test pygmentify.tests --settings="pygmentify.tests.settings"
   
   Creating test database for alias 'default'...
   ..........
   ----------------------------------------------------------------------
   Ran 9 tests in 0.326s
   
   OK
   Destroying test database for alias 'default'...

A bundled settings file allows you to test the code without even creating a Django project.
