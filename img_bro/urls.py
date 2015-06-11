__author__ = 'szymon'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.images_list ),

]