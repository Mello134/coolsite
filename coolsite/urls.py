"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static  # для DEBUG пути
from django.contrib import admin
from django.urls import path
from coolsite import settings  # для DEBUG пути
from men.views import *  # импортировали из men/views.py  - все функции
from django.urls import include  # импорт функции include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('men.urls')),  # путь к путям к приложению men
]

# то есть в режиме отладки когда DEBUG = True
if settings.DEBUG:
    # для debug_toolbar
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    # к путям добавляем путь к статическим данным, графическим данным
    # на реальных серверах обычно это не используется
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound