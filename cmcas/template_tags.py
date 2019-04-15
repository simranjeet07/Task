from django import template

register = template.Library()
register.filter('shorten', shorten)

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter
def upper(value):
    return value.upper()
