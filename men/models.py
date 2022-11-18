from django.db import models

class Men(models.Model):  # наследуем все функции для нашего класса Men от Django класса Model
    # Id прописывать не нужно - Model Это делает автоматически
    title = models.CharField(max_length=255)  # длина 255 символов
    content = models.TextField(blank=True)  # текстовое поле без ограничений, blank=True - поле может быть пустым
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')  # загружать будем в photos/год/месяц/день
    time_create = models.DateTimeField(auto_now_add=True)  # дата время - создание, auto_now_add=True - создастся единожды
    time_update = models.DateTimeField(auto_now=True)  # дата время - изменение, auto_now=True - будет менятся с каждым изменением
    is_publisher = models.BooleanField(default=True)  # default=True

    # с помощью метода запись нашего класса будет выводится по её заголовку
    def __str__(self):
        return self.title


# Create your models here.
