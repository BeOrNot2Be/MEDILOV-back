from django import template

register = template.Library()

@register.inclusion_tag('components/header.html')
def header(page):
    return {"page":page}