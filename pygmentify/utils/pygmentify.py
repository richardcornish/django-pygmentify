from __future__ import unicode_literals

import ast

from django import template
from django.utils.encoding import force_text

from bs4 import BeautifulSoup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name, guess_lexer
from pygments.util import ClassNotFound

register = template.Library()


def bits_to_dict(bits):
    """Convert a Django template tag's kwargs into a dictionary of Python types.

    The only necessary types are number, boolean, list, and string.
    http://pygments.org/docs/formatters/#HtmlFormatter

    from: ["style='monokai'", "cssclass='cssclass',", "boolean='true',", 'num=0,', "list='[]'"]
      to: {'style': 'monokai', 'cssclass': 'cssclass', 'boolean': True, 'num': 0, 'list': [],}
    """
    # Strip any trailing commas
    commaless_bits = [bit[:-1] if bit.endswith(',') else bit for bit in bits]

    # Append 'style=' to any positional arg to create a keyword arg
    cleaned_bits = ['style=' + bit if '=' not in bit else bit for bit in commaless_bits]

    # Create dictionary by splitting on equal signs
    options = dict(bit.split('=') for bit in cleaned_bits)

    for key in options:

        # Coerce string of number to number (templates don't quote numbers)
        if options[key].isdigit():
            options[key] = int(options[key])

        # Coerce string of string of boolean to boolean
        elif options[key].lower() == "'true'":
            options[key] = True
        elif options[key].lower() == "'false'":
            options[key] = False

        # Coerce string of string of list to list
        elif options[key].startswith("'[") and options[key].endswith("]'"):
            options[key] = ast.literal_eval(options[key].strip("'"))

        # Coerce string of string to string
        elif options[key].startswith("'") and options[key].endswith("'"):
            options[key] = options[key].strip("'")

    return options


def to_string(item):
    """Convert a NavigableString to a string."""
    try:  # Python 2
        return unicode(item)
    except NameError:
        return str(item)


def pygmentify(value, **kwargs):
    """Return a highlighted code block with Pygments."""
    soup = BeautifulSoup(value, 'html.parser')
    for pre in soup.find_all('pre'):

        # Get code
        code = ''.join([to_string(item) for item in pre.contents])
        code = code.replace('&lt;', '<')
        code = code.replace('&gt;', '>')
        code = code.replace('&#39;', "'")
        code = code.replace('&quot;', '"')
        code = code.replace('&amp;', '&')

        # Get lexer by language
        lexers = get_all_lexers()
        try:
            class_list = pre['class']
        except IndexError:
            class_list = []
            lexer = guess_lexer(pre, stripall=True)
        for _class in class_list:
            for lexer in lexers:
                short_names = lexer[1]
                for short_name in short_names:
                    if _class == short_name:
                        language = short_name
        try:
            lexer = get_lexer_by_name(language, stripall=True)
        except ClassNotFound:
            lexer = guess_lexer(pre, stripall=True)

        # Get formatter
        html_options = kwargs.get('html_options', {})
        formatter = HtmlFormatter(**html_options)

        # Highlight code
        highlighted = highlight(code, lexer, formatter)
        class_string = ' '.join([_class for _class in class_list])
        highlighted = highlighted.replace(
            '<div class="%s"><pre>' % html_options['cssclass'],
            '<div class="%s"><pre class="%s">' % (html_options['cssclass'], class_string)
        )
        pre.replace_with(highlighted)

    return force_text(soup.encode(formatter=None).strip())
