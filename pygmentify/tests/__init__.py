from __future__ import unicode_literals

from django.template import Context, Template
from django.test import TestCase


class PygmentifyTestCase(TestCase):
    """Pygmentify test cases."""

    def test_pygmentify_html(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify %}"
            '<pre class="html">'
            '<p>Hello, world!</p>'
            "</pre>"
            "{% endpygmentify %}"
        ).render(Context())
        print(out)
        self.assertEqual(out, '<div class="highlight"><pre class="html"><span></span><span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>Hello, world!<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>\n</pre></div>')

    def test_pygmentify_html_kwarg(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify linenos='true' %}"
            '<pre class="html">'
            '<p>Hello, world!</p>'
            "</pre>"
            "{% endpygmentify %}"
        ).render(Context())
        self.assertEqual(out, '<table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="highlight"><pre class="html"><span></span><span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>Hello, world!<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>\n</pre></div>\n</td></tr></table>')

    def test_pygmentify_python(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify %}"
            '<pre class="python">'
            'print("Hello, world!")'
            "</pre>"
            "{% endpygmentify %}"
        ).render(Context())
        self.assertEqual(out, '<div class="highlight"><pre class="python"><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</pre></div>')

    def test_pygmentify_python_arg(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify 'monokai' %}"
            '<pre class="python">'
            'print("Hello, world!")'
            "</pre>"
            "{% endpygmentify %}"
        ).render(Context())
        self.assertEqual(out, '<div class="highlight"><pre class="python"><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</pre></div>')

    def test_pygmentify_python_kwarg(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify style='monokai' %}"
            '<pre class="python">'
            'print("Hello, world!")'
            "</pre>"
            "{% endpygmentify %}"
        ).render(Context())
        self.assertEqual(out, '<div class="highlight"><pre class="python"><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</pre></div>')

    def test_pygmentify_python_kwargs(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify style='monokai' cssclass='cssclass' %}"
            '<pre class="python">'
            'print("Hello, world!")'
            "</pre>"
            "{% endpygmentify %}"
        ).render(Context())
        self.assertEqual(out, '<div class="cssclass"><pre class="python"><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</pre></div>')

    def test_pygmentify_css(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify_css %}"
        ).render(Context())
        self.assertEqual(out, '/static/pygmentify/css/default.min.css')

    def test_pygmentify_css_arg(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify_css 'monokai' %}"
        ).render(Context())
        self.assertEqual(out, '/static/pygmentify/css/monokai.min.css')

    def test_pygmentify_css_kwarg(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify_css style='monokai' %}"
        ).render(Context())
        self.assertEqual(out, '/static/pygmentify/css/monokai.min.css')
