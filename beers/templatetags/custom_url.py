from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name = 'custom_url')
@stringfilter
def get_custom_url(value):
    if ' ' in str(value):
        sections = value.split(' ')
        sections = [section.lower() for section in sections]
        y = "_".join(sections)
        return y
    return value
