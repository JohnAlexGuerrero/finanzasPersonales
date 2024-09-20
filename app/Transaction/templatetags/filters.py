from django import template
from datetime import datetime

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

@register.filter(name='pct')
def pct(value):
    pct_value = (178000 - value) / 178000
    return f'{(pct_value * 100):,.0f}'

@register.filter(name="group_datetime")
def group_datetime(date):
    date_str = 'Today'
    today = datetime.now()

    if date.strftime('%w') != today.strftime('%w'):
        date_str = f'{date.strftime('%A')}, {date.strftime('%d')} {date.strftime('%b')} {date.strftime('%Y')}'
        
    return date_str