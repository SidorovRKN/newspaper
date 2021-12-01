from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *




def index(request):
    posts = News.objects.all()
    context = {
        'posts': posts,
        'title': 'главная страница',
        'cat_selected': 0,
    }
    return render(request, 'news/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post': post,

        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'news/post.html', context=context)



def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404
    context = {
        'posts': posts,
        'title': 'рубрика',
        'cat_selected': cat_id,
    }
    return render(request, 'news/index.html', context=context)


def about(request):
    return render(request, 'news/about.html', {'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
