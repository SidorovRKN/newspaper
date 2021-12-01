from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [
        {'title': 'o saite', 'url_name': 'about'},
        {'title': 'Dobavit statyu', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Log In', 'url_name': 'login'},
       ]


def index(request):
    posts = News.objects.all()
    context =  {'menu': menu, 'posts': posts, 'title': 'главная страница'}
    return render(request, 'news/index.html', context=context)

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def about(request):
    return render(request, 'news/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

