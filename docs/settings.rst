.. _settings:

Settings
********

The template tag offers one setting that nests options as a dictionary. By default, it is:

.. code-block:: python

   PYGMENTIFY = {
       'style': 'default',
       'cssclass': 'highlight',
       'minify': True,
   }

The keys of the dictionary correspond to the keyword argument options of Pygments's |HtmlFormatterClass|_, which means you're free to use any of the 20+ options. The default options are:

.. |HtmlFormatterClass| replace:: ``HtmlFormatterClass``
.. _HtmlFormatterClass: http://pygments.org/docs/formatters/#HtmlFormatter

* ``style`` is a string indicating the `Pygments style class <http://pygments.org/docs/styles/>`_ to use.
* ``cssclass`` is a string indicating the class of the ``<div>`` element that wraps the highlighted code.
* ``minify`` is a boolean indicating the serving of a minified CSS file. It does not have an equivalent in the Pygments's ``HtmlFormatterClass`` and is unique to Pygmentify.

The up-to-date list of styles is in the `Pygments repository <https://bitbucket.org/birkenfeld/pygments-main/src/a042025b350cd9c9461f7385d9ba0f13cdb01bb9/pygments/styles/__init__.py?at=default&fileviewer=file-view-default>`_, but generally speaking, the styles from which to choose are:

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

Previously only two settings, ``PYGMENTIFY_CSSCLASS`` and ``PYGMENTIFY_STYLE``, were offered, corresponding respectively to the ``cssclass`` and ``style`` keys in ``PYGMENTIFY``.
