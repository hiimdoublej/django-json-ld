# django-json-ld

This is a django template tag to help developers render [structured data](https://developers.google.com/search/docs/guides/intro-structured-data) tags inside their django templates.

## Installation
Install using `pip`:
```
pip install django-json-ld
```

Add `django_json_ld` to `INSTALLED_APPS` in `settings.py`:
```
INSTALLED_APPS = [
    # Other apps...
    'django_json_ld',
]
```

## Settings
You can override the following options in settings.py:

`JSON_LD_CONTEXT_ATTRIBUTE`: the context attribute name used in `django_json_ld`'s Class-Based Views (CBV). Defaults to `'sd'`.

`JSON_LD_MODEL_ATTRIBUTE`: the model attribute name used by `JsonLdDetailView` to get the model's structured data. Defaults to `'sd'`.

`JSON_LD_DEFAULT_CONTEXT`: default json-ld context when using `django_json_ld`'s CBVs. Defaults to `'https://schema.org'`.

`JSON_LD_DEFAULT_TYPE`: default json-ld type when using `django_json_ld`'s CBVs. Defaults to `'Thing'`.

`JSON_LD_GENERATE_URL`: generate json-ld's `url` field when using `django_json_ld`'s CBVs. Defaults to `True`.


## Usage Example
Assuming you have a structured data `sd` like the following in your context (copied from the link above).
```
sd = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "url": "http://www.example.com",
  "name": "Unlimited Ball Bearings Corp.",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-401-555-1212",
    "contactType": "Customer service"
    }
}
```
Then, in your template:
```
{% load render_json_ld from django_json_ld %}
{% render_json_ld sd %}
```
Would render into:
```
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "url": "http://www.example.com",
  "name": "Unlimited Ball Bearings Corp.",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-401-555-1212",
    "contactType": "Customer service"
  }
}
</script>
```

### Class-Based View example

views.py
```python
from django_json_ld.views import JsonLdDetailView

class ProductDetailView(JsonLdDetailView):
    model=Product
```

models.py
```python
class Product(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'))
    
    @property
    def sd(self):
        return {
            "@type": 'Product',
            "description": self.description,
            "name": self.name,
        }
```

By using  `{% render_json_ld sd %}`, as explained in the previous example, would render into something like:

```json
{
    "@context":"https://schema.org",    
    "@type":"Product",
    "name":"The Product",
    "description":"A great product.",
    "url":"http://example.org/products/1/the-product/"
}
```

In the above example `JsonLdDetailView` adds `sd` to `ProductDetailView`'s context, using `Product`'s own `sd` property. The `url` is generated automatically by `JsonLdDetailView`. This behaviour is configurable through settings.
