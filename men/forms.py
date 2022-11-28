from django import forms  # модуль forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

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


# Форма регистрации
class RegisterUserForm(UserCreationForm):  # создаём экземпляр формы регистрации пользователя на базе UserCreationForm
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User  # связь с моделью User (стандартная)
        # отображаем поля модели User
        # название полей - в админке - посмотреть код страницы - name
        fields = ('username', 'email', 'password1', 'password2')


# Форма авторизации
class LoginUserForm(AuthenticationForm):  # AuthenticationForm - стандартная форма
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form.input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form.input'}))
