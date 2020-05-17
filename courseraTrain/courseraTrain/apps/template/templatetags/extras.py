from django import template

register = template.Library()


@register.filter
def inc(value, increment):
    return int(value) + int(increment)


@register.simple_tag
def division(divisible, divider, to_int=False):
    try:
        print(divider, divisible)
        ans = float(divisible) / float(divider)
        return int(ans) if to_int else ans
    except ValueError:
        raise template.TemplateSyntaxError()

