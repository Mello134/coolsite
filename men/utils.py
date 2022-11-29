from django.db.models import Count
from django.core.cache import cache
from men.models import Category

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 20  # Количество отображаемых элементов на странице (пагинация)
    # метод будет создавать context (передаваемые параметры) - для шаблонов
    def get_user_context(self, **kwargs):
        # формируем начальный словарь context - из именованных параметров переданной методу g_u_c
        context = kwargs
        cats = cache.get('cats')  # вызываем cache, пытаемся прочитать из cats из кэша
        if not cats: # если cats не были прочитаны
            #  читаем данные из БД
            cats = Category.objects.annotate(Count('men'))  # количество постов в каждой рубрике
            cache.set('cats', cats, 60)  # записываем кэш на 60 сек

        # копируем всё меню в новую переменную (когда будет вызываться метод get_user_context)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:  # если не авторизован:
            user_menu.pop(1)  # удаляем 'Добавить Меню' строчку полностью с URLom
        context['menu'] = user_menu  # {'menu':'user_menu'} / {'ключ':'значение'}

        context['cats'] = cats
        if 'cat_selected' not in context:  # если cat_selected нету в context
            context['cat_selected'] = 0  # создаём cat_selected и присваиваем значение 0
        return context  # вернём словарь context(словарь передаваемых параметры в шаблоны)
