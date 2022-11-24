from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404  # импортировали
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView  # функции представления

from .forms import *  # из forms.py импортируем все классы форм
from .models import *  # импортируем все модели из men/models.py


# в целях обучения, как передавать параметры в шаблон из функции представления
side = [{'title': 'Все категории', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Домашняя страницы', 'url_name': 'home'},
        ]


# класс - функция представления домашней страницы
class MenHome(ListView):  # ListView - класс представление / наш дочерний класс MenHome от класса ListView /
    model = Men  # связываемся с моделью Men (будет отображать список статей)
    template_name = 'men/index.html'
    # Все записи в модели Men те. object_list или Men.objects.all()
    context_object_name = 'posts'  # к object_list можно обращаться как к posts

    # Передаём параметры в шаблон (функция формирует и динамический и статический контекст)
    def get_context_data(self, *, object_list=None, **kwargs):
        # берём уже существующий контекст get_context_data =  ('posts')
        # **kwargs - распаковываем словарь kwargs
        context = super().get_context_data(**kwargs)  # на этом моменте у нас уже есть posts
        context['side'] = side  # добавим в словарь context - список side и даём ему имя side
        context['title'] = 'Главная страница'  # добавим в словарь передаваемых параметров title
        context['cat_selected'] = 0
        return context  # передаём все параметры в шаблон posts+title+side

    def get_queryset(self):
        # возвращаем то какие записи должны быть прочитаны из модели Men
        # будут прочитаны и отображены только с галочкой
        return Men.objects.filter(is_publisher=True)


# функция представления домашней страницы категорий(музыканты актёры)
class MenCategory(ListView):  # ListView - класс представление / наш дочерний класс MenCategory от класса ListView /
    model = Men  # связываемся с моделью Men (будет отображать список статей)
    template_name = 'men/index.html'
    # Все записи в модели Men те. object_list или Men.objects.all()
    context_object_name = 'posts'  # к object_list можно обращаться как к posts
    allow_empty = False

    # возвращаем только те категории которые опубликованы и те что выбрали по слагу
    # когда будет формироваться экземпляр запроса MenCategory, то через ссылку self
    def get_queryset(self):
        # Записи по фильтру 1 - self обращаемся к словарю kwargs, берём параметр маршрута из path - cat_slug,
        # is_publisher = True - только опубликованные
        # cat__slug - через cat из Men, ссылаемся уже в Category - и обращаемся к Category -полю slug
        return Men.objects.filter(cat__slug=self.kwargs['cat_slug'], is_publisher=True)

    # Передаём параметры в шаблон (функция формирует и динамический и статический контекст)
    def get_context_data(self, *, object_list=None, **kwargs):
        # берём уже существующий контекст get_context_data =  ('posts')
        # **kwargs - распаковываем словарь kwargs
        context = super().get_context_data(**kwargs)  # на этом моменте у нас уже есть posts
        context['side'] = side  # добавим в словарь context - список side и даём ему имя side
        # Добавим в словарь передаваемых параметров title
        # posts - object_list или Men.objects.all() - но с фильтром по слагу категории
        # str(context['posts'][0].cat) - обращаемся к первой записи из post, по параметру cat
        # - тот в свою очередь обращается в нужную категорию, а категория отображается по своему имени
        # - из-за get absolut. В итоге - выводится просто имя категории.
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['posts'][0].cat_id - аналогично с title - только будет выводится id категории
        context['cat_selected'] = context['posts'][0].cat_id
        return context  # передаём все параметры в шаблон posts+title+side






# def index(request):  # функция отображения главной страница
#     # Берем все записи из модели Men, помещаем в переменную
#     posts = Men.objects.all()
#
#     # context - словарь передаваемых параметров
#     context = {
#         'posts': posts,  # все записи модели Men - title, content, photo...
#         'title': 'Главная страница',  # название страницы
#         'cat_selected': 0,  # будут отображаться все записи
#     }
#     return render(request, 'men/index.html', context=context)


# #def show_category(request, cat_slug):  # обязательно доп параметр cat_slug
#     posts = Men.objects.filter(cat__slug=cat_slug)  # cat   '__'   slug!!! cat__slug=cat_slug

    # # для получения cat_selected ------------------------------------
    # cat_one_record = Category.objects.get(slug=cat_slug)  # получили 1 полную запись Category
    # cat_selected = cat_one_record.pk  # получили id или pk этой записи!
    # # для получения cat_selected ------------------------------------
    #
    # if len(posts) == 0:  # Если количество постов 0
    #     raise Http404()  # отобразится страница 404 - def pageNotFound(если DEBUG = False)
    #     # если DEBUG = True - нам покажет обычную страницу ошибки, с причиной ошибки

    # # context - словарь передаваемых параметров
    # context = {
    #     'posts': posts,  # cat_id - к какой категории принадлежит запись в таблице Men
    #     'title': 'Отображение по рубрикам',  # название страницы
    #     'cat_selected': cat_selected,  # cat_selected - принимает значение cat_slug записи Men
    # }
    # # Шаблон домашней страницы, несмотря на то что это категории
    # return render(request, 'men/index.html', context=context)


def about(request):  # о странице
    # (request, 'men/templates/men/about.html', {'ключ':'значение'})
    return render(request, 'men/about.html', {'title': 'О сайте'})

# Функция представления страницы формы добавления поста
class AddPage(CreateView):
    form_class = AddPostForm  # связываемся с нашим классом формы AddPostForm из forms.py
    template_name = 'men/addpage.html'  # ссылка на шаблон
    success_url = reverse_lazy('home')  # после добавления формы, перенаправит по пути path name='home'

    # Передаём параметры в шаблон (функция формирует и динамический и статический контекст)
    def get_context_data(self, *, object_list=None, **kwargs):
        # берём уже существующий контекст get_context_data =  ('posts')
        # **kwargs - распаковываем словарь kwargs
        context = super().get_context_data(**kwargs)  # на этом моменте у нас уже есть posts
        context['side'] = side  # добавим в словарь context - список side и даём ему имя side
        context['title'] = 'Добавление статьи'  # добавим в словарь передаваемых параметров title
        return context  # передаём все параметры в шаблон posts+title+side


# def addpage(request):
    # # 2) если уже была какая-то отправка
    # if request.method == 'POST':  # если уже что то пытались отправить
        # # request.FILES - передаём список файлов, которые были отправлены на сервер из формы
        # form = AddPostForm(request.POST, request.FILES)  # ?создаём экземпляр класса AddPostForm
        # if form.is_valid():  # если заполнено правильно
            # # print(form.cleaned_data)  - проверка в терминале
            # form.save()  # добавляем запись в базу данных Men - заменяет всю конструкцию try-except
            # return redirect('home')  # если добавление прошло, то возвращает path = name='home'
    # # 1) при первом открывании формы
    # else:
        # form = AddPostForm()  # пустая форма
    # return render(request, 'men/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('<h1>Страница Обратной связи</h1>')


def login(request):
    return HttpResponse('<h1>Авторизация</h1>')


def pageNotFound(request, exception):
    # exception - если произошли какие-то исключения, мы должны их обработать
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_slug):  # обязательно добавь доп параметр post_slug
#     # если slug есть то есть есть запись в модели Men, то покажет страницу если нет то 404
    # post = get_object_or_404(Men, slug=post_slug)

    # context = {
    #     'post': post,  # все записи модели Men - title, content, photo...
    #     'title': post.title,  # название страницы = название поста
    #     'cat_selected': post.cat_id,  # cat_id - в модели, поле cat (id автоматом делает django)
    # }
    # return render(request, 'men/post.html', context=context)


# отображение поста - функция представления
class ShowPost(DetailView):  # создаём класс ShowPost, наследуемся от DetailView
    model = Men  # связываемся с моделью Men
    template_name = 'men/post.html'  # ссылка на шаблон
    slug_url_kwarg = 'post_slug'  # чтобы post/<slug:post_slug>/ - стандартно искал бы post/<slug:slug>/
    context_object_name = 'post'

    # Передаём параметры в шаблон (функция формирует и динамический и статический контекст)
    def get_context_data(self, *, object_list=None, **kwargs):
        # берём уже существующий контекст get_context_data =  ('posts')
        # **kwargs - распаковываем словарь kwargs
        context = super().get_context_data(**kwargs)  # на этом моменте у нас уже есть posts
        context['side'] = side  # добавим в словарь context - список side и даём ему имя side
        context['title'] = context['post']  # Имя поста в title
        # context['cat_selected'] = object_list.cat_id # НЕРАБОТАЕТ - ДОБАВЬ ПОТОМ
        return context  # передаём все параметры в шаблон posts+title+side


