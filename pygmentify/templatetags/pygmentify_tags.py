from __future__ import unicode_literals

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template import TemplateSyntaxError
from django.utils.encoding import force_text
from django.utils.html import escape

from bs4 import BeautifulSoup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.util import ClassNotFound

from .. import settings

register = template.Library()


@register.simple_tag
def pygmentify_css(*args):
    """Return the URL of the Pygments CSS file with optional theme."""
    if len(args) > 1:
        raise TemplateSyntaxError('"pygmentify_css" tag takes exactly zero or one arguments.')
    arg = args[0] if args else settings.PYGMENTIFY_STYLE
    return staticfiles_storage.url('pygmentify/css/%s.min.css' % arg)


@register.filter
def pygmentify(value, arg=''):
    """Return a highlighted code block with Pygments."""
    args_list = [a for a in arg.split(',') if a]

    # Get style
    try:
        style = args_list[0]
    except IndexError:
        style = settings.PYGMENTIFY_STYLE

    # Get cssclass
    try:
        cssclass = args_list[1]
    except IndexError:
        cssclass = settings.PYGMENTIFY_CSSCLASS

    soup = BeautifulSoup(value, 'html.parser')
    for pre in soup.find_all('pre'):
        try:
            language = pre['class'][0].replace('language-', '', 1)
            try:
                lexer = get_lexer_by_name(language, stripall=True)
            except ClassNotFound:
                lexer = guess_lexer(pre, stripall=True)
        except IndexError:
            lexer = guess_lexer(pre, stripall=True)
        formatter = HtmlFormatter(style=style, cssclass=cssclass)
        pygments_soup = BeautifulSoup(highlight(pre.string, lexer, formatter), 'html.parser')
        pre.clear()
        pre.append(soup.new_tag('code'))
        for content in reversed(pygments_soup.pre.contents):
            if content.string is not None:
                content.string.replace_with(escape(content.string))
            pre.code.insert(0, content)
        pre.wrap(soup.new_tag('div', **{'class': cssclass}))

    return force_text(soup.encode(formatter=None))
