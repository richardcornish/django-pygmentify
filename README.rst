Django Pygmentify
*****************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-pygmentify.svg
.. _PyPI version: https://pypi.python.org/pypi/django-pygmentify

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-pygmentify.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-pygmentify

**Django Pygmentify** is a `Django template filter <https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/>`_ application to highlight code with `Pygments <http://pygments.org/>`_.

It is an alternative to `Django Pygments <https://github.com/od-eon/django-pygments>`_, which hasn't been updated in several years.

* `Package distribution <https://pypi.python.org/pypi/django-pygmentify>`_
* `Code repository <https://github.com/richardcornish/django-pygmentify>`_
* `Documentation <https://django-pygmentify.readthedocs.io/>`_
* `Tests <https://travis-ci.org/richardcornish/django-pygmentify>`_

Install
=======

.. code-block:: bash

   $ pip install django-pygmentify

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'pygmentify',
   ]

Usage
=====

.. code-block:: html

   {% load pygmentify_tags %}

   <link rel="stylesheet" href="{% pygmentify_css %}">
   
   {% filter pygmentify %}
   <pre class="python"><code>
   print('Hello, world!')
   </code></pre>
   {% endpygmentify %}

Result:

.. code-block:: html

   <div class="highlight"><pre class="python"><code><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
   </code></pre></div>
