from django.contrib import admin
from .models import *  # импортируем все классы men/models.py


class MenAdmin(admin.ModelAdmin):
    # список отображаемых столбцов в админ-панели
    list_display = ('id', 'title', 'time_create', 'photo', 'is_publisher')
    # список полей на которые можно кликнуть - для редактирования
    list_display_links = ('id', 'title')
    # список полей - ко которым можно вести поиск
    search_fields = ('title', 'content')
    # редактирование поля публикации - в списке - в админке
    list_editable = ('is_publisher',)  # запятая - если 1 поле!
    # фильтрование по полям - публикация, время изменения.
    list_filter = ('is_publisher', 'time_create')
    prepopulated_fields = {'slug': ('title',)}  # автозаполнение слага по имени поста


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
