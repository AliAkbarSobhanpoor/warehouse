from django import template

register = template.Library()

@register.filter
def abs_number(number:int):
    return abs(number)

@register.filter
def thousand_separators(value:int):
    return f"{value:,}"