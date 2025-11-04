from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
    Разбивает строку по разделителю
    Использование: {{ value|split:"," }}
    """
    return value.split(key)

@register.filter(name='trim')
def trim(value):
    """Удаляет пробелы в начале и конце строки"""
    if value:
        return value.strip()
    return value