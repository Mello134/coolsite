from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404  # импортировали

# Create your views here.
def index(request):  # главная страница
    return HttpResponse("<h1>Страница приложения men</h1>")

def categories(request, catid):  # категории
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2022:  # если год больше 2022
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    # exception - если произошли какието исключения, мы должны их обработать
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')