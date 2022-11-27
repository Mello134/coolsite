from django.urls import path, re_path

from .views import *



urlpatterns = [
    # путь('url/', функция, name='имя для пути'),
    # MenHome - ссылаемся на класс представления as_view()-вызываем функцию представления!
    path('', MenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MenCategory.as_view(), name='category'),

]
