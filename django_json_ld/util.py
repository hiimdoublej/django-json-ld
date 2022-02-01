from collections.abc import Mapping

from django.utils.functional import Promise
from django.utils.encoding import force_str
from django.core.serializers.json import DjangoJSONEncoder


def validate_sd(sd):
    if sd and not isinstance(sd, Mapping):
        err = 'Invalid type for provided structured data, expected "dict", got {}'.format(type(sd))
        return False, err
    return True, None


def build_absolute_uri(request):
    return request.build_absolute_uri()


class LazyEncoder(DjangoJSONEncoder):
    """
    Force lazy strings to text

    see: https://stackoverflow.com/a/31746279/4249576
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_str(obj)
        return super(LazyEncoder, self).default(obj)
