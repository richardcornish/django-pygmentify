.. _usage:

Usage
*****

HTML
====

Load the template tags.

.. code-block:: django

   {% load pygmentify_tags %}

Use the ``{% filter pygmentify %}`` template tag to covert HTML into Pygments HTML.

.. code-block:: django

   {% filter pygmentify %}
   <pre class="python"><code>
   print('Hello, world!')
   </code></pre>
   {% endfilter %}

Result:

.. code-block:: html

   <div class="highlight"><pre class="python"><code><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
   </code></pre></div>

The ``{% filter pygmentify %}`` template tag expects an opening ``<pre>`` tag with a ``class`` attribute of the programming language that you are using. For example, ``<pre class="python">`` uses `Python <http://pygments.org/docs/lexers/#pygments.lexers.python.PythonLexer>`_, and ``<pre class="html">`` uses `HTML <http://pygments.org/docs/lexers/#pygments.lexers.html.HtmlLexer>`_.

If no CSS class is specified, the template tag makes a `best guess <http://pygments.org/docs/api/#pygments.lexers.guess_lexer>`_ using heuristics of the code inside of the ``<pre>`` element. If multiple CSS classes are specified, the first one is selected. The template tag also strips a possible ``language-`` prefix that could be prepended to the first class.

Pygments's default behavior strips your customized ``<pre class="...">`` tag and replaces it with a plain ``<pre>`` tag. The template tag undoes this unacceptable behavior and preserves the customized ``<pre class="...">`` tag. Additionally, the inner contents of the ``<pre class="...">`` are wrapped in a semantic ``<code>`` element if no ``code`` tags are present.

Consult the `Pygments documentation <http://pygments.org/docs/lexers/>`_ for all language short names. There's even a `Django <http://pygments.org/docs/lexers/#pygments.lexers.templates.DjangoLexer>`_ template one.

CSS
===

Use the ``{% pygmentify_css %}`` template tag to output the URL of the CSS file.

.. code-block:: django

   <link rel="stylesheet" href="{% pygmentify_css %}">

Result:

.. code-block:: html

   <link rel="stylesheet" href="/static/pygmentify/css/default.min.css">

The way that Pygments generates CSS is awkward. Rather than provide CSS files, Pygments abstracts a more generalized style language into `Python classes to create styles <http://pygments.org/docs/styles/>`_ that can be used with formatters other than HTML. Therefore, the template tag provides exports of the default styles using the |pygmentize|_ command and |cleancss|_ library.

.. |pygmentize| replace:: ``pygmentize``
.. _pygmentize: http://pygments.org/docs/cmdline/#generating-styles

.. |cleancss| replace:: ``clean-css``
.. _cleancss: https://www.npmjs.com/package/clean-css

.. code-block:: bash

   pygmentize -S <style> -f html > <style>.css
   cleancss <style>.css -o <style>-min.css

Please remember to put the ``<link>`` tag in the ``<head>`` of your document.

Examples
========

.. code-block:: django

   {% load pygmentify_tags %}

   <link rel="stylesheet" href="{% pygmentify_css %}">

   {% filter pygmentify %}
   <pre class="python"><code>
   print('Hello, world!')
   </code></pre>
   {% endfilter %}

Customize the behavior by passing the name of a style into the ``{% pygmentify_css %}`` tag and into the ``{% filter pygmentify %}`` filter.

.. code-block:: django

   {% load pygmentify_tags %}

   <link rel="stylesheet" href="{% pygmentify_css 'monokai' %}">

   {% filter pygmentify:'monokai' %}
   <pre class="python"><code>
   print('Hello, world!')
   </code></pre>
   {% endfilter %}

Additionally customize the CSS class of the ``<div>`` that wraps the highlighted code by passing a second positional argument to ``{% filter pygmentify %}``.

.. code-block:: django

   {% filter pygmentify:'monokai,bettercssclass' %}
   <pre class="python"><code>
   print('Hello, world!')
   </code></pre>
   {% endfilter %}

If you customize the style, please ensure you pass the same argument, e.g. ``'monokai'``, to *both* the ``{% pygmentify_css %}`` and ``{% filter pygmentify %}`` tags. You might see unexpected behavior otherwise because "`not all lexers might support every style <http://pygments.org/docs/styles/>`_," meaning styles are guaranteed to work fully only when the lexer assigns to tokens HTML classes that correspond to the class selectors in the CSS file. Therefore, you're probably better off customizing the style by changing the :ref:`settings` of the project. Template tag arguments take precedence over settings. Also see :ref:`settings` for creating your own styles.

If you use the `pipe syntax <https://docs.djangoproject.com/en/1.10/ref/templates/language/#filters>`_, e.g. ``{{ post.body|pygmentify }}``, ensure that the variable contains HTML either natively or by conversion (by, say `Markdown <https://pythonhosted.org/Markdown/>`_) because the template tag will look for the HTML outlined earlier.
