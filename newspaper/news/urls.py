from django.urls import path

from news.views import *

urlpatterns = [
    path('', index),
    path('cats/', categories)
]
