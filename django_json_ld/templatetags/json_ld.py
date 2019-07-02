import json

from django import template
from django.conf import settings as django_settings
from django.utils.safestring import mark_safe
from django.template import TemplateSyntaxError

from ..util import LazyEncoder, validate_sd, build_absolute_uri
from .. import settings

register = template.Library()

empty_input_choice = settings.EMPTY_INPUT_RENDERING


@register.simple_tag(takes_context=True)
def render_json_ld(context, structured_data):
    # validate and throw error if sd is invalid
    is_valid, err = validate_sd(structured_data)
    if not is_valid:
        raise TemplateSyntaxError(err)
    # do empty input rendering stuff here
    if len(structured_data) == 0:
        if empty_input_choice == 'strict':
            err = 'Empty structured_data provided under strict render policy.'
            err += ' Consider changing JSON_LD_EMPTY_INPUT_RENDERING setting to other values.'
            raise TemplateSyntaxError(err)
        elif empty_input_choice == 'silent':
            return ''
        elif empty_input_choice == 'generate_thing':
            structured_data = {
                "@context": settings.DEFAULT_CONTEXT,
                "@type": settings.DEFAULT_TYPE,
                "url": build_absolute_uri(context['request']),
            }
    indent = settings.JSON_INDENT if django_settings.DEBUG else None
    nl = '' if indent is None else '\n'
    dumped = json.dumps(structured_data, ensure_ascii=False, cls=LazyEncoder, indent=indent, sort_keys=True)
    text = "<script type=\"application/ld+json\">{nl}{dumped}{nl}</script>".format(
        nl=nl, dumped=dumped)
    return mark_safe(text)
