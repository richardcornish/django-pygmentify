from __future__ import unicode_literals

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

from .. import settings
from ..utils.pygmentify import bits_to_dict, pygmentify as _pygmentify

register = template.Library()


class PygmentifyCssNode(template.Node):
    def __init__(self, **kwargs):
        self.options = kwargs

    def render(self, context):
        style = self.options['style']
        path = '.min' if settings.PYGMENTIFY_MINIFY == True else ''
        return staticfiles_storage.url('pygmentify/css/%s%s.css' % (style, path))


@register.tag
def pygmentify_css(parser, token):

    # Convert tag kwargs to dictionary
    bits = token.split_contents()
    remaining_bits = bits[1:]
    remaining_bits = ['style=' + bit if '=' not in bit else bit for bit in remaining_bits]
    tag_options = bits_to_dict(remaining_bits)

    # Update settings with tag options
    options = settings.PYGMENTIFY.copy()
    options.update(tag_options)

    return PygmentifyCssNode(**options)


class PygmentifyNode(template.Node):
    def __init__(self, nodelist, **kwargs):
        self.nodelist = nodelist
        self.options = kwargs

    def render(self, context):
        output = self.nodelist.render(context)
        return _pygmentify(output, **self.options)


@register.tag
def pygmentify(parser, token):

    # Convert tag kwargs to dictionary
    bits = token.split_contents()
    remaining_bits = bits[1:]
    remaining_bits = ['style=' + bit if '=' not in bit else bit for bit in remaining_bits]
    tag_options = bits_to_dict(remaining_bits)

    # Update settings with tag options
    options = settings.PYGMENTIFY.copy()
    options.update(tag_options)

    nodelist = parser.parse(('endpygmentify',))
    parser.delete_first_token()
    return PygmentifyNode(nodelist, **options)
