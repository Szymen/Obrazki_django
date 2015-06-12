__author__ = 'szymon'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.images_list ),
    url(r'^add',views.add_new),
    url(r'^added-new',views.added_new),
]