from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *  # импортируем все классы men/models.py


class MenAdmin(admin.ModelAdmin):
    # список отображаемых столбцов в админ-панели
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_publisher')
    # список полей на которые можно кликнуть - для редактирования
    list_display_links = ('id', 'title')
    # список полей - ко которым можно вести поиск
    search_fields = ('title', 'content')
    # редактирование поля публикации - в списке - в админке
    list_editable = ('is_publisher',)  # запятая - если 1 поле!
    # фильтрование по полям - публикация, время изменения.
    list_filter = ('is_publisher', 'time_create')
    prepopulated_fields = {'slug': ('title',)}  # автозаполнение слага по имени поста
    # список полей которые стоит отображать в форме редактирования
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_publisher', 'time_create', 'time_update')
    # не редактируемые поля (только после этой строчки можно добавить из в fields)
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True  # панель сверху(дубль)

    # отобажение миниматюр фото в админке
    def get_html_photo(self, object):
        if object.photo:  # если фото есть
            return mark_safe(f"<img src='{object.photo.url}' width=50>")  # mark_safe - не экранирует теги

    get_html_photo.short_description = "Миниатюра"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # ЗАПЯТАЯ В КОНЦЕ- при одном поле
    prepopulated_fields = {'slug': ('name',)}  # автозаполнение слага по имени категории


# Register your models here.
# регистрируем в админке - модель Men
# регистрируем класс отображения в админке - MenAdmin
admin.site.register(Men, MenAdmin)
admin.site.register(Category, CategoryAdmin)

# заголовки в админке
admin.site.site_title = 'Админ-панель Mello'
admin.site.site_header = 'Админ-панель Mello'
