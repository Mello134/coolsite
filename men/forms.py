from django import forms  # модуль forms
from django.core.exceptions import ValidationError

from .models import *  # все модели models.py


# Форма загрузки статьи
class AddPostForm(forms.ModelForm):  # создаётся экземпляр формы (когда отображается пустая форма в браузере)
    def __init__(self, *args, **kwargs):  # вызывается конструктор
        super().__init__(*args, **kwargs)  # вызывается конструктор базового класса Men
        self.fields['cat'].empty_label = 'Категория не выбрана'  # для поля cat меняем свойство - emply_label


    class Meta:
        model = Men  # связь с моделью Men
        # отображаем  поля модели Men (кроме тек что заполняются автоматически)
        # вместо списка можно сделать '__all__' - но не рекомендуется
        fields = ['title', 'slug', 'content', 'photo', 'is_publisher', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # валидация - title
    def clean_title(self):
        title = self.cleaned_data['title']  # получаем данные по заголовку
        if len(title) > 200:  # если больше 200 символов
            # генерируется исключение - выводит сообщение об ошибке
            raise ValidationError('Длина превышает 200 символов')

        return title  # иначе (если всё ок < 200) - просто возвращается заголовок
