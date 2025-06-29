from django import template


register = template.Library()

# obsolete due to calculations in contexts.py
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity, size_modifier, wax_modifier):
    return (price * size_modifier * wax_modifier) * quantity
