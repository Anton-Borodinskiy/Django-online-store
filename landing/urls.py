from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path("", views.home, name="home"),#Ссылка(home страница)
    path("clothing/", views.clothing, name="clothing"),  # Ссылка(home страница)
    path("shoes/", views.shoes, name="shoes"),  # Ссылка(home страница)
    path("accesories/", views.accesories, name="accesories"),  # Ссылка(home страница)

]