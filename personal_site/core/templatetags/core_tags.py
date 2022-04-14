from django import template

from utils.menu import SIDEBAR_MENU

register = template.Library()


@register.simple_tag(name='get_sidebar_menu')
def get_sidebar_menu(name=None):
    if not name:
        return SIDEBAR_MENU
    else:
        return [i for i in SIDEBAR_MENU if i[name] == name][0]
