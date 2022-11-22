from django import forms  # модуль forms
from .models import *  # все модели models.py


# Форма загрузки статьи
# аттрибуты(поля) совпадают с полями в Men
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cools': 60, 'rows': 10}), label='Контент')
    # required=False необязательное поле, initial=True изначально галочка стоит
    is_publisher = forms.BooleanField(label='Публикация', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    # time_create , time_update - автоматически будут меняется в классе Men
