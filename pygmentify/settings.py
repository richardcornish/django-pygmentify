from __future__ import unicode_literals

from django.conf import settings


PYGMENTIFY = {
    'style': 'default',
    'cssclass': 'highlight'
}

PYGMENTIFY_MINIFY = getattr(settings, 'PYGMENTIFY_MINIFY', True)
