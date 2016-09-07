.. _usage:

Usage
*****

HTML
====

Use the ``{% pygmentify %}`` template tag to covert HTML into Pygments HTML.

.. code-block:: html

   {% pygmentify %}
   <pre class="python"><code>
       print('Hello, world!')
   </code></pre>
   {% endpygmentify %}

Result:

.. code-block:: html

   <div class="highlight"><pre><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
   </pre></div>

The ``{% pygmentify %}`` template tag expects an opening ``<pre>`` tag with a ``class`` attribute of the programming language that you are using. `Python <http://pygments.org/docs/lexers/#pygments.lexers.python.PythonLexer>`_ expects ``<pre class="python">``, and `HTML <http://pygments.org/docs/lexers/#pygments.lexers.html.HtmlLexer>`_ expects ``<pre class="html">``.

If no CSS class is specified, the template tag makes a best guess using heuristics of the code inside of the ``<pre>`` element. If multiple CSS classes are specified, the first one is selected. The template tag also finds a possible ``language-`` prefix that could be prepended to the first class.

Consult the `Pygments documentation <http://pygments.org/docs/lexers/>`_ for all lexers with corresponding languages. There's even a `Django <http://pygments.org/docs/lexers/#pygments.lexers.templates.DjangoLexer>`_ template one.

CSS
===

Use the ``{% pygmentify_css %}`` template tag to output the URL of the CSS file.

.. code-block:: html

   <link rel="stylesheet" href="{% pygmentify_css %}">

Result:

.. code-block:: html

   <link rel="stylesheet" href="/static/css/default.min.css">

The way that Pygments generates CSS is awkward. Rather than provide CSS files, Pygments abstracts a more generalized style language into `Python classes to create styles <http://pygments.org/docs/styles/>`_ that can be used with formatters other than HTML. Therefore, the template tag provides exports of the default styles (using |pygmentize|_) and their respective minified versions (using |cleancss|_).

Please remember to put the ``<link>`` tag in the ``<head>`` of your document.

.. |pygmentize| replace:: ``pygmentize``
.. _pygmentize: http://pygments.org/docs/cmdline/#generating-styles

.. |cleancss| replace:: ``clean-css``
.. _cleancss: https://www.npmjs.com/package/clean-css

Examples
========

.. code-block:: html

   {% load pygmentify_tags %}

   <link rel="stylesheet" href="{% pygmentify_css %}">

   {% pygmentify %}
   <pre class="python"><code>
       print('Hello, world!')
   </code></pre>
   {% endpygmentify %}

Customize the behavior by passing the name of a style into the ``{% pygmentify_css %}`` tag and into the ``{% pygmentify %}`` filter.

.. code-block:: html

   {% load pygmentify_tags %}

   <link rel="stylesheet" href="{% pygmentify_css 'monokai' %}">

   {{ post.body|pygmentify:'monokai' }}

Additionally customize the CSS class of the ``<div>`` that wraps the highlighted code by passing a second argument to the ``{% pygmentify %}`` filter.

.. code-block:: html

   {{ post.body|pygmentify:"monokai,bettercssclass" }}

If you use the pipe (``|``) syntax on a context variable, ensure that the variable contains HTML either natively or by conversion (by, say `Markdown <https://pythonhosted.org/Markdown/>`_) because the template tag will look for the HTML outlined earlier.

Bear in mind that you're probably better off customizing the behavior by changing the :ref:`settings` of the project, but the template tag is flexible too. Template tag arguments take precedence over settings.
