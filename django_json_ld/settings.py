from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


CONTEXT_ATTRIBUTE = getattr(settings, 'JSON_LD_CONTEXT_ATTRIBUTE', 'sd')
MODEL_ATTRIBUTE = getattr(settings,   'JSON_LD_MODEL_ATTRIBUTE', 'sd')

DEFAULT_CONTEXT = getattr(settings, 'JSON_LD_DEFAULT_CONTEXT', 'https://schema.org')
DEFAULT_TYPE = getattr(settings,    'JSON_LD_DEFAULT_TYPE', 'Thing')
GENERATE_URL = getattr(settings,    'JSON_LD_GENERATE_URL', True)

valid_empty_input_rendering_settings = [
    'strict', 'silent', 'generate_thing'
]

EMPTY_INPUT_RENDERING = getattr(settings, 'JSON_LD_EMPTY_INPUT_RENDERING', 'strict')

if EMPTY_INPUT_RENDERING not in valid_empty_input_rendering_settings:
    err = 'Invalid value for JSON_LD_EMPTY_INPUT_RENDERING setting.'
    err += 'Expected one of {}, but got "{}"'.format(
        valid_empty_input_rendering_settings,
        EMPTY_INPUT_RENDERING
    )
    raise ImproperlyConfigured(err)
