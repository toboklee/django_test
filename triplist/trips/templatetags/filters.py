from django import template

register = template.Library()


@register.filter
def calc_price(value, arg):
    currency = arg[:1]
    price = float(arg.replace(',', '')[1:])
    return ''.join([currency, str(price * int(value))])


@register.filter
def remaining_people(value, arg):
    if arg:
        return int(arg) - int(value)
    else:
        return value