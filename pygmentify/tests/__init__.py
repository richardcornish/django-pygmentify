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
        print(out)
        self.assertEqual(out, '<div class="highlight"><pre><span></span><span class="k">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>\n</pre></div>\n')

    def test_pygmentify_css(self):
        out = Template(
            "{% load pygmentify_tags %}"
            "{% pygmentify_css %}"
        ).render(Context())
        print(out)
        self.assertEqual(out, '/static/css/default.min.css')
