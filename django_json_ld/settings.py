from django.conf import settings


CONTEXT_ATTRIBUTE = getattr(settings, 'JSON_LD_CONTEXT_ATTRIBUTE', 'sd')
MODEL_ATTRIBUTE = getattr(settings,   'JSON_LD_MODEL_ATTRIBUTE', 'sd')

DEFAULT_CONTEXT = getattr(settings, 'JSON_LD_DEFAULT_CONTEXT', 'https://schema.org')
DEFAULT_TYPE = getattr(settings,    'JSON_LD_DEFAULT_TYPE', 'Thing')
GENERATE_URL = getattr(settings,    'JSON_LD_GENERATE_URL', True)
