"""Z_HLove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from  love import  views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^h_isaccpet_z/love', views.home),
    url(r'^hAccpetz/loveStartTime/', views.loveTime),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
