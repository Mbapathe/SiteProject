from django import template

register = template.Library()

@register.filter
def truncatewords_slice(value, arg):
    return " ".join(value.split()[arg:])
