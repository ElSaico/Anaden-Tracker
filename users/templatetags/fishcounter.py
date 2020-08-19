from django import template

register = template.Library()

@register.filter(is_safe=True)
def fishCounter(actual_catch):
    sum = 0
    for i in fish:
        sum += i.actual_catch
    return sum
