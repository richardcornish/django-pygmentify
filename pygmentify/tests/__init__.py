from __future__ import unicode_literals

from django.template import Context, Template
from django.test import TestCase


class PygmentifyTestCase(TestCase):
    """Pygmentify test cases."""

    def test_pygmentify(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% filter pygmentify %}"
            '<pre class="python">'
            'print("Hello, world!")'
            "</pre>"
            "{% endfilter %}"
        ).render(Context())
        self.assertEqual(out, '<div class="highlight"><pre class="python"><code><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</code></pre></div>')

    def test_pygmentify_monokai(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% filter pygmentify:'monokai' %}"
            '<pre class="python">'
            'print("Hello, world!")'
            "</pre>"
            "{% endfilter %}"
        ).render(Context())
        self.assertEqual(out, '<div class="highlight"><pre class="python"><code><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</code></pre></div>')

    def test_pygmentify_monokai_cssclass(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% filter pygmentify:'monokai,cssclass' %}"
            '<pre class="python">'
            'print("Hello, world!")'
            "</pre>"
            "{% endfilter %}"
        ).render(Context())
        self.assertEqual(out, '<div class="cssclass"><pre class="python"><code><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</code></pre></div>')

    def test_pygmentify_css(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify_css %}"
        ).render(Context())
        self.assertEqual(out, '/static/pygmentify/css/default.min.css')

    def test_pygmentify_css_monokai(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify_css 'monokai' %}"
        ).render(Context())
        self.assertEqual(out, '/static/pygmentify/css/monokai.min.css')
