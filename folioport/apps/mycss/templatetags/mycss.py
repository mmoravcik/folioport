import uuid

from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag()
def mycss(cache=1):
    css = settings.MYCSS_PATH + 'mycss.css'
    if not cache:
        css = "%s?u=%s" % (css, str(uuid.uuid4()))
    return css