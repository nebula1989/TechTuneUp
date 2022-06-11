from django import template
from datetime import date

register = template.Library()


@register.simple_tag(name='current_year')
def get_current_year():

    year = date.today().year

    return year
