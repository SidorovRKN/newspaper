from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Страница приложения news')


def categories(request, catid):
    return HttpResponse(f'<h1>Страница приложения news</h1><p>{catid}</p>')