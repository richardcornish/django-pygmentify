.. _usage:

Usage
*****

HTML
====

Load the template tags.

.. code-block:: django

   {% load pygmentify_tags %}

Use the ``{% pygmentify %}`` template tag to covert HTML into Pygments HTML.

.. code-block:: django

   {% pygmentify %}
   <pre class="python">
   print('Hello, world!')
   </pre>
   {% endpygmentify %}

Result:

.. code-block:: html

   <div class="highlight"><pre class="python"><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
   </pre></div>

The ``{% pygmentify %}`` template tag expects an opening ``<pre>`` tag with a ``class`` attribute of the programming language that you are using that matches against the `short name of the corresponding Pygment lexer <http://pygments.org/docs/lexers/>`_. For example, ``<pre class="python">`` uses the `Python <http://pygments.org/docs/lexers/#pygments.lexers.python.PythonLexer>`_ lexer, and ``<pre class="html">`` uses the `HTML <http://pygments.org/docs/lexers/#pygments.lexers.html.HtmlLexer>`_ lexer to highlight code.

If no CSS class is present, the template tag makes a `best guess <http://pygments.org/docs/api/#pygments.lexers.guess_lexer>`_ using heuristics of the code between the ``<pre>`` tags. If multiple CSS classes are present, the classes are collected into a list and are iterated against `all available lexers <http://pygments.org/docs/lexers/>`_.

Pygments's default behavior strips your customized ``<pre class="...">`` tag and replaces it with a plain ``<pre>`` tag. The template tag undoes this behavior and preserves the customized ``<pre class="...">`` tag.

See the `Pygments documentation <http://pygments.org/docs/lexers/>`_ for all language short names. There's even a `Django <http://pygments.org/docs/lexers/#pygments.lexers.templates.DjangoLexer>`_ template one.

CSS
===

Use the ``{% pygmentify_css %}`` template tag to output the URL of the CSS file.

.. code-block:: django

   <link rel="stylesheet" href="{% pygmentify_css %}">

Result:

.. code-block:: html

   <link rel="stylesheet" href="/static/pygmentify/css/default.min.css">

The default output of the style file is the minified version.

The way that Pygments generates CSS is awkward. Rather than provide CSS files, Pygments abstracts a more generalized style language into `Python classes to create styles <http://pygments.org/docs/styles/>`_ that can be used with formatters other than HTML. Therefore, the template tag provides exports of the default styles using the |pygmentize|_ command and |cleancss|_ library.

.. |pygmentize| replace:: ``pygmentize``
.. _pygmentize: http://pygments.org/docs/cmdline/#generating-styles

.. |cleancss| replace:: ``clean-css``
.. _cleancss: https://www.npmjs.com/package/clean-css

.. code-block:: bash

   $ pygmentize -S <style> -f html > <style>.css

.. code-block:: bash

   $ cleancss <style>.css -o <style>.min.css

Please remember to put the ``<link>`` tag in the ``<head>`` of your document.

Minimalist example
==================

The bare minimum to highlight your code is to use the ``{% pygmentify %}`` tag and to load a corresponding style with the ``{% pygmentify_css %}`` tag.

.. code-block:: django

   {% load pygmentify_tags %}

   <link rel="stylesheet" href="{% pygmentify_css %}">

   {% pygmentify %}
   <pre class="python">
   print('Hello, world!')
   </pre>
   {% endpygmentify %}

The ``default.min.css`` style file will be used in this example.

Please ensure that the code to highlight contains HTML either natively or by conversion (by, say `Markdown <https://pythonhosted.org/Markdown/>`_) because the template tag will look for fully rendered HTML.

Customize with positional arguments
===================================

Customize the behavior of the ``{% pygmentify_css %}`` and ``{% pygmentify %}`` tags by passing the name of a style as a positional argument.

.. code-block:: django

   {% load pygmentify_tags %}

   <link rel="stylesheet" href="{% pygmentify_css 'monokai' %}">

   {% pygmentify 'monokai' %}
   <pre class="python">
   print('Hello, world!')
   </pre>
   {% endpygmentify %}

The ``monokai.min.css`` style file will be used in this example.

The name of a style is the only possible positional argument available to ``{% pygmentify_css %}`` and ``{% pygmentify %}``.

If you customize the style, please ensure you pass the same argument, e.g. ``'monokai'``, to *both* the ``{% pygmentify_css %}`` and ``{% pygmentify %}`` tags. You might see unexpected behavior otherwise because "`not all lexers might support every style <http://pygments.org/docs/styles/>`_," meaning styles are guaranteed to work fully only when the lexer assigns to tokens HTML classes that correspond to the class selectors in the CSS file. Therefore, you're probably better off customizing the style by changing the :ref:`settings` of the project. Template tag arguments take precedence over settings. Also see :ref:`settings` for creating your own styles.

Customize with keyword arguments
================================

Additionally customize the behavior of the ``{% pygmentify_css %}`` and ``{% pygmentify %}`` tags with keyword arguments.

The ``{% pygmentify_css %}`` can accept the ``style`` and ``minify`` keyword arguments.

.. code-block:: django

   {% pygmentify_css style='monokai' minify='false' %}

The ``monokai.css`` style file will be used in this example.

Note that because Django's template language is not Python, the ``{% pygmentify_css %}`` "keyword arguments" are expected to be strings. Therefore, most notably, use ``'true'`` or ``'false'`` for the ``minify`` keyword argument. You will probably want the minified file, so use ``'true'``--or even better omit the keyword argument all together because the default style file to use is the minified file.

Therefore:

.. code-block:: django

   {% pygmentify_css style='default' minify='true' %}

is equivalent to...

.. code-block:: django

   {% pygmentify_css 'default' %}

which is also equivalent to...

.. code-block:: django

   {% pygmentify_css %}

Additionally, the ``{% pygmentify %}`` tag accepts all available options of Pygments's ``HtmlFormatter`` class, such as ``style`` and ``linenos``, as keyword arguments.

.. code-block:: django

   {% pygmentify style='monokai' cssclass='bettercssclass' linenos='true' linenostart=0 %}
   <pre class="python">
   print('Hello, world!')
   </pre>
   {% endpygmentify %}

Again, because Django's template language is not Python, template tags expect either a string or a number as a keyword argument. Therefore, in instances when Pygments's ``HtmlFormatter`` constructor expects a Python data type, such as a string, number, boolean, or list, the value of the keyword argument should be the equivalent string or number. For example, pass ``'true'`` as the equivalent of ``True`` or ``'[...]'`` as the equivalent of ``[...]``. Numbers can be left as is. All keyword arguments are later coerced into Python data types.

See `Pygments's documentation <http://pygments.org/docs/formatters/#HtmlFormatter>`_ on the ``HtmlFormatter`` class for all available keyword arguments.
