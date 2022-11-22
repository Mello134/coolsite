from django.db import models
from django.urls import reverse


# Create your models here.
class Men (models.Model):  # наследуем все функции для нашего класса Men от Django класса Model
    # Id прописывать не нужно - Model Это делает автоматически
    title = models.CharField(max_length=255, verbose_name='Заголовок')  # длина 255 символов
    # unique=True - поле уникально, db_index=True - индексируемое (для ускорения поиска, verbose_name - отображение в адм.
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')  # текстовое поле без ограничений, blank=True - поле может быть пустым
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')  # загружать будем в photos/год/месяц/день
    # дата время - создание, auto_now_add=True - создастся единожды
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    # дата время - изменение, auto_now=True - будет меняться с каждым изменением
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_publisher = models.BooleanField(default=True, verbose_name='Публикация')  # default=True
    # cat_id - id добавится автоматом
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    # с помощью метода запись нашего класса будет выводиться по её заголовку
    def __str__(self):
        return self.title

    # функция формирования маршрута к ссылке
    def get_absolute_url(self):  # self - ссылка на один экземпляр(строку) таблицы модели
        # получаем путь('path name=post, 'post/<slug:post_slug>/) = 127/post/butusov)
        return reverse('post', kwargs={'post_slug': self.slug})  # self.slug - атрибут slug

    class Meta:  # специальный класс - для отображения модели
        verbose_name = 'Популярные личности'  # отображение в админке вместо 'Mens'
        verbose_name_plural = 'Популярные личности'  # отображение во множественном числе
        ordering = ['time_create', 'title']  # сортировка, сначала по дате создания, потом по имени


class Category(models.Model):
    # db_index - для того чтобы поле было индексированным, поиск по небу будет происходить быстрей
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    # будем обращаться к категории по полю name
    def __str__(self):
        return self.name

    # функция формирования маршрута к ссылке
    def get_absolute_url(self):
        # получаем путь('path name=category, 'category/<slug:cat_slug>/' = 127/category/muzikanty)
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:  # специальный класс - для отображения модели
        verbose_name = 'Категория'  # отображение в админке вместо 'Category'
        verbose_name_plural = 'Категории'  # отображение во множественном числе
        ordering = ['id']  # сортировка, сначала по id
