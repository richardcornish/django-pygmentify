.. _settings:

Settings
********

The template tag offers two settings. By default, they are:

.. code-block:: python

   PYGMENTIFY_CSSCLASS = 'highlight'

   PYGMENTIFY_STYLE = 'default'

``PYGMENTIFY_CSSCLASS`` is a string of the `CSS class <http://pygments.org/docs/formatters/#HtmlFormatter>`_ of the ``<div>`` element that wraps the highlighted code. 

``PYGMENTS_STYLE`` is a string of the `Pygments style class <http://pygments.org/docs/styles/>`_ to use. The up-to-date list of styles is in the `Pygments repository <https://bitbucket.org/birkenfeld/pygments-main/src/a042025b350cd9c9461f7385d9ba0f13cdb01bb9/pygments/styles/__init__.py?at=default&fileviewer=file-view-default>`_, but generally speaking, the styles from which to choose are:

- ``algol_nu``
- ``algol``
- ``autumn``
- ``borland``
- ``bw``
- ``colorful``
- ``default``
- ``emacs``
- ``friendly``
- ``fruity``
- ``igor``
- ``lovelace``
- ``manni``
- ``monokai``
- ``murphy``
- ``native``
- ``paraiso-dark``
- ``paraiso-light``
- ``pastie``
- ``perldoc``
- ``rrt``
- ``tango``
- ``trac``
- ``vim``
- ``vs``
- ``xcode``

Preview these styles by visiting any of the Pygments `demo entries <http://pygments.org/demo/>`_.

By setting ``PYGMENTS_STYLE`` once, the template tag automatically sets the correct Pygments HTML output *and* corresponding CSS to use.

Both of these settings are available on a per-template basis. See examples in :ref:`Usage` for details.
