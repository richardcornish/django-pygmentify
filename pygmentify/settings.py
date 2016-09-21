from __future__ import unicode_literals

from django.conf import settings


PYGMENTIFY_STYLE = getattr(settings, 'PYGMENTIFY_STYLE', 'default')

PYGMENTIFY_CSSCLASS = getattr(settings, 'PYGMENTIFY_CSSCLASS', 'highlight')
