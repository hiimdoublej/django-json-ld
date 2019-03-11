from django.views import generic

from . import settings


DEFAULT_STRUCTURED_DATA = {}
if settings.DEFAULT_CONTEXT:
    DEFAULT_STRUCTURED_DATA["@context"] = settings.DEFAULT_CONTEXT
if settings.DEFAULT_TYPE:
    DEFAULT_STRUCTURED_DATA["@type"] = settings.DEFAULT_TYPE


class JsonLdContextMixin(object):
    """
    CBV mixin which sets structured data within the view's context
    """
    structured_data = {}

    def __init__(self):
        super(JsonLdContextMixin, self).__init__()
        instance_structured_data = DEFAULT_STRUCTURED_DATA.copy()
        instance_structured_data.update(self.structured_data)
        self.structured_data = instance_structured_data

    def get_structured_data(self):
        if settings.GENERATE_URL and "url" not in self.structured_data:
            self.structured_data["url"] = self.request.build_absolute_uri(self.request.get_full_path())
        return self.structured_data.copy()

    def get_context_data(self, **kwargs):
        context = super(JsonLdContextMixin, self).get_context_data(**kwargs)
        context[settings.CONTEXT_ATTRIBUTE] = self.get_structured_data()
        return context


class JsonLdView(JsonLdContextMixin, generic.View):
    """
    Render a view with structured data.

    Set `structured_data` with structured data constant fields.
    Override `get_structured_data` for any dynamic fields.
    """


class JsonLdSingleObjectMixin(JsonLdContextMixin):
    """
    CBV mixin which sets structured data for a single object within the context
    """
    def get_structured_data(self):
        super(JsonLdSingleObjectMixin, self).get_structured_data()
        model_structured_data = getattr(self.object, settings.MODEL_ATTRIBUTE)
        self.structured_data.update(model_structured_data)
        return self.structured_data.copy()


class JsonLdDetailView(JsonLdSingleObjectMixin, generic.DetailView):
    """
    Render a "detail" view with structured data taken from object.

    By default implement property `sd` in the model to return structured data in a dict.
    """
