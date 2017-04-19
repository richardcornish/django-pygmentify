from __future__ import unicode_literals

from django.conf import settings


PYGMENTIFY = {
    'style': 'default',
    'cssclass': 'highlight',
    'minify': True,
}

pygmentify_user = getattr(settings, 'PYGMENTIFY', {})

PYGMENTIFY.update(pygmentify_user)
