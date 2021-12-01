from django import template
from news.models import *

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('news/list_categories.html')
def show_categories(sort=None,cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats":cats, "cat_selected": cat_selected}

@register.inclusion_tag('news/menu.html')
def show_menu():
    menu = [
        {'title': 'o saite', 'url_name': 'about'},
        {'title': 'Dobavit statyu', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Log In', 'url_name': 'login'},
    ]

    return {"menu": menu}
