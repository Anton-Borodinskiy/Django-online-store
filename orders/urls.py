from django.urls import path, include
from django.conf.urls import re_path
from . import views

urlpatterns = [

    path("basket_adding/", views.basket_adding, name='basket_adding'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
]