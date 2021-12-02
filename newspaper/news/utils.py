from django.db.models import Count
from .models import *
menu = [
        {'title': 'o saite', 'url_name': 'about'},
        {'title': 'Dobavit statyu', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Log In', 'url_name': 'login'},
    ]

class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('news'))
        context['cats'] = cats
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
