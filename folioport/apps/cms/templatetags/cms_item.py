from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def cms_item_render(context, item):
    return item.render(context)


@register.simple_tag(takes_context=True)
def cms_container_render(context, container):
    return container.render(context)