from django.views.generic.detail import DetailView

from . import settings


INITIAL_STRUCTURED_DATA = {}
if settings.DEFAULT_CONTEXT:
    INITIAL_STRUCTURED_DATA["@context"] = settings.DEFAULT_CONTEXT
if settings.DEFAULT_TYPE:
    INITIAL_STRUCTURED_DATA["@type"] = settings.DEFAULT_TYPE


class JsonLdContextMixin(object):
    """
    CBV mixin which sets sets structured data within the context
    """
    structured_data = INITIAL_STRUCTURED_DATA

    def get_structured_data(self, instance=None):
        if settings.GENERATE_URL:
            self.structured_data["url"] = self.request.build_absolute_uri(self.request.get_full_path())

        if instance:
            model_structured_data = getattr(instance, settings.MODEL_ATTRIBUTE)
            self.structured_data.update(model_structured_data)

        return self.structured_data.copy()

    def get_context_data(self, **kwargs):
        context = super(JsonLdContextMixin, self).get_context_data(**kwargs)
        try:
            obj = kwargs.get('object', self.object)
        except AttributeError:
            obj = None
        context[settings.CONTEXT_ATTRIBUTE] = self.get_structured_data(instance=obj)
        return context


class JsonLdDetailView(JsonLdContextMixin, DetailView):
    """
    Render a "detail" view with structured data taken from of an object.

    By default implement property `sd` in the model to return structured data in a dict.
    """
