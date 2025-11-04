from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
    Разбивает строку по разделителю
    Использование: {{ value|split:"," }}
    """
    return value.split(key)