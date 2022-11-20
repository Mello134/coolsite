from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404  # импортировали
from .models import *  # импортируем все модели из men/models.py


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):  # функция отображения главной страница
    # Берем все записис модели, помещаем в переменную
    posts = Men.objects.all()
    # (request, 'путь к шаблону', передаваемые параметры параметры)
    return render(request, 'men/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def categories(request, catid):  # категории
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:  # если год больше 2022
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    # exception - если произошли какие-то исключения, мы должны их обработать
     return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):  # главная страница
    # (request, 'men/templates/men/about.html', {'ключ':'значение'})
    return render(request, 'men/about.html', {'menu': menu, 'title': 'О сайте'})