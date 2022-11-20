from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404  # импортировали
from .models import *  # импортируем все модели из men/models.py

# список - для navbar
menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
]


def index(request):  # функция отображения главной страница
    # Берем все записи из модели Men, помещаем в переменную
    posts = Men.objects.all()
    # Берем все записи из модели категории, помещаем в переменную
    cats = Category.objects.all()

    # context - словарь передаваемых параметров
    context = {
        'posts': posts,  # все записи модели Men - title, content, photo...
        'cats': cats,  # все записи модели категории
        'menu': menu,  # navbar - title, url_name
        'title': 'Главная страница',  # название страницы
        'cat_selected': 0,  # будут отображаться все записи
    }
    return render(request, 'men/index.html', context=context)


def about(request):  # о странице
    # (request, 'men/templates/men/about.html', {'ключ':'значение'})
    return render(request, 'men/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('<h1>Страница создания статьи</h1>')


def contact(request):
    return HttpResponse('<h1>Страница Обратной связи</h1>')


def login(request):
    return HttpResponse('<h1>Авторизация</h1>')


def pageNotFound(request, exception):
    # exception - если произошли какие-то исключения, мы должны их обработать
     return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):  # обязательно добавь доп параметр post_id
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, cat_id):  # обязательно добавь доп параметр cat_id
    # Берем только cat_id (номер категории)
    posts = Men.objects.filter(cat_id=cat_id)
    # Берем все записи из модели категории, помещаем в переменную
    cats = Category.objects.all()

    if len(posts) == 0:  # Если количество постов 0
        raise Http404()  # отобразится страница 404 - def pageNotFound(если DEBUG = False)
        # если DEBUG = True - нам покажет обычную страницу ошибки, с причиной ошибки

    # context - словарь передаваемых параметров
    context = {
        'posts': posts,  # cat_id - к какой категории принадлежит запись в таблице Men
        'cats': cats,  # все записи модели категории
        'menu': menu,  # navbar - title, url_name
        'title': 'Отображение по рубрикам',  # название страницы
        'cat_selected': cat_id,  # cat_selected - принимает значение cat_id записи Men
    }
    # Шаблон домашней страницы, несмотря на то что это категории
    return render(request, 'men/index.html', context=context)
