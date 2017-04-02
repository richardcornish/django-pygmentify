from __future__ import unicode_literals

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

from ..utils.pygmentify import bits_to_dict, pygmentify as _pygmentify
from .. import settings

register = template.Library()


class PygmentifyCssNode(template.Node):
    def __init__(self, **kwargs):
        self.css_options = kwargs['css_options']

    def render(self, context):
        style = self.css_options['style']
        path = '.min' if self.css_options['minify'] else ''
        return staticfiles_storage.url('pygmentify/css/%s%s.css' % (style, path))


@register.tag
def pygmentify_css(parser, token):
    bits = token.split_contents()
    remaining_bits = bits[1:]
    css_options = bits_to_dict(remaining_bits)

    # Get default settings if necessary
    if 'style' not in css_options:
        css_options['style'] = settings.PYGMENTIFY_STYLE
    # Get minify status
    if 'minify' not in css_options:
        css_options['minify'] = True
    if not isinstance(css_options['minify'], bool):
        raise template.TemplateSyntaxError('%r tag\'s "minify" keyword argument should be "true", "false", or omitted.' % bits[:1])

    return PygmentifyCssNode(css_options=css_options)


class PygmentifyNode(template.Node):
    def __init__(self, nodelist, **kwargs):
        self.nodelist = nodelist
        self.html_options = kwargs['html_options']

    def render(self, context):
        output = self.nodelist.render(context)
        return _pygmentify(output, html_options=self.html_options)


@register.tag
def pygmentify(parser, token):
    bits = token.split_contents()
    remaining_bits = bits[1:]
    html_options = bits_to_dict(remaining_bits)

    # Get default settings if necessary
    if 'style' not in html_options:
        html_options['style'] = settings.PYGMENTIFY_STYLE
    if 'cssclass' not in html_options:
        html_options['cssclass'] = settings.PYGMENTIFY_CSSCLASS

    nodelist = parser.parse(('endpygmentify',))
    parser.delete_first_token()
    return PygmentifyNode(nodelist, html_options=html_options)
