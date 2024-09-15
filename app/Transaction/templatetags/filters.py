from django import template

register = template.Library()

@register.filter(name='format_value_total')
def format_value_total(value):
    return f'$ {value:,.0f}'