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
