from django import template  # модуль template djando
from men.models import *  # все наши модели

register = template.Library()


# функция будет возвращать все наши категории
@register.simple_tag(name='getcats')  # Превращаем ф в тег. simple_tag - простой тег, из класса Library
def get_categories(filter=None):  # стандартно фильтр не выбран
    if not filter:  # если фильтр не выбран
        return Category.objects.all()  # вернуть все записи категории
    else:  # иначе
        return Category.objects.filter(pk=filter)  # вернуть запись по фильтру id


# тег будет возвращать весь список категорий в sidebar в виде html отрывка
#
# 3 имя шаблона, куда будет передаваться параметр cats
# list_categories.html - необходимо создать в templates/men
@register.inclusion_tag('men/list_categories.html')
def show_categories(sort=None, cat_selected = 0):  # 4 будет возвращать полноценную html страницу list_categories.html
    if not sort:  # если сортировка не определена
        cats = Category.objects.all()  # 1 читает все категории
    else:  # если сортировка определена
        cats = Category.objects.order_by(sort)  # делаем сортировку, которую указали
    return {'cats': cats, 'cat_selected': cat_selected}  # 2 возвращает 2 параметра Категории, и cat_selected


# тег menu
@register.inclusion_tag('men/list_menu.html')
def show_menu():  # 4 будет возвращать полноценную html страницу list_menu.html
    menu = [{'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить статью', 'url_name': 'add_page'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            {'title': 'Войти', 'url_name': 'login'},
            ]
    return {'menu': menu}  # # navbar - title, url_name - возвращаемые параметры в шаблон
