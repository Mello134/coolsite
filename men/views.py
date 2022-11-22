from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404  # импортировали

from .forms import *  # из forms.py импортируем все классы форм
from .models import *  # импортируем все модели из men/models.py


def index(request):  # функция отображения главной страница
    # Берем все записи из модели Men, помещаем в переменную
    posts = Men.objects.all()

    # context - словарь передаваемых параметров
    context = {
        'posts': posts,  # все записи модели Men - title, content, photo...
        'title': 'Главная страница',  # название страницы
        'cat_selected': 0,  # будут отображаться все записи
    }
    return render(request, 'men/index.html', context=context)


def about(request):  # о странице
    # (request, 'men/templates/men/about.html', {'ключ':'значение'})
    return render(request, 'men/about.html', {'title': 'О сайте'})


def addpage(request):
    # 2) если уже была какая-то отправка
    if request.method == 'POST':  # если уже что то пытались отправить
        form = AddPostForm(request.POST)  # ?создаём экземпляр класса AddPostForm
        if form.is_valid():  # если заполнено правильно
            # принт это временно, чтобы понять что отобразится (в терминале)
            # print(form.cleaned_data)
            #
            try:  # патаемся
                Men.objects.create(**form.cleaned_data)  # добавляем запись в базу данных Men
                return redirect('home')  # если добавление прошло, то возвращает path = name='home'
            except:  # исключение (если не получилось добавить
                # общая ошибка на странице формы
                # чтобы её отобразить в шаблоне необходимо добавить
                form.add_error(None, 'Ошибка добавления поста')  # общая ошибка на странице формы
    # 1) при первом открывании формы
    else:
        form = AddPostForm()  # пустая форма
    return render(request, 'men/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('<h1>Страница Обратной связи</h1>')


def login(request):
    return HttpResponse('<h1>Авторизация</h1>')


def pageNotFound(request, exception):
    # exception - если произошли какие-то исключения, мы должны их обработать
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):  # обязательно добавь доп параметр post_slug
    # если slug есть то есть есть запись в модели Men, то покажет страницу если нет то 404
    post = get_object_or_404(Men, slug=post_slug)

    context = {
        'post': post,  # все записи модели Men - title, content, photo...
        'title': post.title,  # название страницы = название поста
        'cat_selected': post.cat_id,  # cat_id - в модели, поле cat (id автоматом делает django)
    }
    return render(request, 'men/post.html', context=context)


def show_category(request, cat_slug):  # обязательно доп параметр cat_slug
    posts = Men.objects.filter(cat__slug=cat_slug)  # cat   '__'   slug!!! cat__slug=cat_slug

    # для получения cat_selected ------------------------------------
    cat_one_record = Category.objects.get(slug=cat_slug)  # получили 1 полную запись Category
    cat_selected = cat_one_record.pk  # получили id или pk этой записи!
    # для получения cat_selected ------------------------------------

    if len(posts) == 0:  # Если количество постов 0
        raise Http404()  # отобразится страница 404 - def pageNotFound(если DEBUG = False)
        # если DEBUG = True - нам покажет обычную страницу ошибки, с причиной ошибки

    # context - словарь передаваемых параметров
    context = {
        'posts': posts,  # cat_id - к какой категории принадлежит запись в таблице Men
        'title': 'Отображение по рубрикам',  # название страницы
        'cat_selected': cat_selected,  # cat_selected - принимает значение cat_slug записи Men

    }
    # Шаблон домашней страницы, несмотря на то что это категории
    return render(request, 'men/index.html', context=context)
