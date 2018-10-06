.. _settings:

Settings
********

The template tag offers two settings. By default, they are:

.. code-block:: python

   PYGMENTIFY = {
       'style': 'default',
       'cssclass': 'highlight'
   }

   PYGMENTIFY_MINIFY = True

``PYGMENTIFY``
==============

A dictionary corresponding to the keyword argument options of Pygments's |HtmlFormatterClass|_, which means you're free to use any of the 20+ options. The default options are:

.. |HtmlFormatterClass| replace:: ``HtmlFormatterClass``
.. _HtmlFormatterClass: http://pygments.org/docs/formatters/#HtmlFormatter

* ``style`` is a string indicating the `Pygments style class <http://pygments.org/docs/styles/>`_ to use.
* ``cssclass`` is a string indicating the class of the ``<div>`` element that wraps the highlighted code.

The up-to-date list of styles is in the `Pygments repository <https://bitbucket.org/birkenfeld/pygments-main/src/7941677dc77d4f2bf0bbd6140ade85a9454b8b80/pygments/styles/?at=default>`_, but generally speaking, the styles from which to choose are:

* ``algol``
* ``algol_nu``
* ``arduino``
* ``autumn``
* ``borland``
* ``bw``
* ``colorful``
* ``default``
* ``emacs``
* ``friendly``
* ``fruity``
* ``igor``
* ``lovelace``
* ``manni``
* ``monokai``
* ``murphy``
* ``native``
* ``paraiso-dark``
* ``paraiso-light``
* ``pastie``
* ``perldoc``
* ``rrt``
* ``tango``
* ``trac``
* ``vim``
* ``vs``
* ``xcode``

Preview these styles by visiting any of the Pygments `demo entries <http://pygments.org/demo/>`_.

This setting is also available on a per-template basis, but by setting the value of the ``style`` key of ``PYGMENTIFY`` once, the template tag automatically sets the correct Pygments HTML output *and* corresponding CSS to use. See examples in :ref:`Usage` for details.

If you want to `create your own style <http://pygments.org/docs/styles/#creating-own-styles>`_, follow the Pygments documentation by creating a ``Style`` class, registering it as a plugin, and passing its ``name`` attribute to the value of the ``style`` key of the ``PYGMENTIFY`` setting.

``PYGMENTIFY_MINIFY``
=====================

* A boolean indicating the serving of a minified CSS file. The app serves the minified file by default.
