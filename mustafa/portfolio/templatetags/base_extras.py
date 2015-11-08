from django import template
import portfolio

register = template.Library()


@register.simple_tag
def get_version():
    return portfolio.__version__
