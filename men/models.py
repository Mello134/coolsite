from django.db import models
from django.urls import reverse


# Create your models here.
class Men (models.Model):  # наследуем все функции для нашего класса Men от Django класса Model
    # Id прописывать не нужно - Model Это делает автоматически
    title = models.CharField(max_length=255)  # длина 255 символов
    content = models.TextField(blank=True)  # текстовое поле без ограничений, blank=True - поле может быть пустым
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')  # загружать будем в photos/год/месяц/день
    # дата время - создание, auto_now_add=True - создастся единожды
    time_create = models.DateTimeField(auto_now_add=True)
    # дата время - изменение, auto_now=True - будет меняться с каждым изменением
    time_update = models.DateTimeField(auto_now=True)
    is_publisher = models.BooleanField(default=True)  # default=True
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # cat_ig - id добавится автоматом

    # с помощью метода запись нашего класса будет выводиться по её заголовку
    def __str__(self):
        return self.title

    # функция формирования маршрута к ссылке
    def get_absolute_url(self):  # self - ссылка на один экземпляр(строку) таблицы модели
        return reverse('post', kwargs={'post_id': self.pk})  # self.pk - атрибут pk


class Category(models.Model):
    # db_index - для того чтобы поле было индексированным, поиск по небу будет происходить быстрей
    name = models.CharField(max_length=100, db_index=True)

    # будем обращаться к категории по полю name
    def __str__(self):
        return self.name

    # функция формирования маршрута к ссылке
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
