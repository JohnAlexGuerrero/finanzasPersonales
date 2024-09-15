from django import template

register = template.Library()

@register.filter(name='format_value_total')
def format_value_total(value):
    return f'$ {value:,.0f}'

@register.filter(name='capitalize')
def capitalize(text):
    description_capitalize = ''
    
    for t in text.split(' '):
        description_capitalize += t.capitalize() + ' ' 
    return description_capitalize