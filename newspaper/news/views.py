from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *


class NewsMain(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def index(request):
#     posts = News.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'news/index.html', context=context)

class ShowPost(DetailView):
    model = News
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context

# def show_post(request, post_slug):
#     post = get_object_or_404(News, slug=post_slug)
#
#     context = {
#         'post': post,
#
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'news/post.html', context=context)


class NewsCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


# def show_category(request, cat_id):
#     posts = News.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404
#     context = {
#         'posts': posts,
#         'title': 'рубрика',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'news/index.html', context=context)


def about(request):
    return render(request, 'news/about.html', {'title': 'О сайте'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'news/addpage.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#
#
#     else:
#         form = AddPostForm()
#     return render(request, 'news/addpage.html', {'form': form, 'title': 'добавление статьи'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
