"""weblog URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^logapp/', 'logapp.views.index', name='index'),
    url(r'^fetch_web/', 'logapp.views.fetch_web', name='fetch_web'),
    url(r'^fetch_web_item/', 'logapp.views.fetch_web_item', name='fetch_web_item'),
    url(r'^fetch_db/', 'logapp.views.fetch_db', name='fetch_db'),
    url(r'^fetch_db_item/', 'logapp.views.fetch_db_item', name='fetch_db_item'),
    url(r'^admin/', include(admin.site.urls)),
]
