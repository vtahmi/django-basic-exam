from  django import template

register = template.Library()

@register.filter
def times_per_month(value):
    return value * 4

@register.filter
def habit_status(frequency):
    if frequency >= 5:
        return "Intensive"
    elif frequency >= 3:
        return "Regular"
    else:
        return "Light"