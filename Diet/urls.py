"""Diet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from diet_planapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index', index, name='index'),
    path(r'signup', signup, name='signup'),
    path(r'login', login, name='login'),
    path(r'fill_form/', fill_form, name='fill_form'),
    path(r'logout', logout, name='logout'),
    path(r'update_info/', update_info, name='update_info'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

