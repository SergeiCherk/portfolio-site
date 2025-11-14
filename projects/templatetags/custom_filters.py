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

@register.filter(name='floordiv')
def floordiv(value, arg):
    """Целочисленное деление"""
    try:
        return int(value) // int(arg)
    except (ValueError, ZeroDivisionError, TypeError):
        return 0

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
