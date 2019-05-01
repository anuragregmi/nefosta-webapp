from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_absolute_uri(context, url):
    return context.get('request').build_absolute_uri(url)
