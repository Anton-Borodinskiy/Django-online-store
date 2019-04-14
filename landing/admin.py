from django.contrib import admin
from .models import *

class SubscriberAdmin (admin.ModelAdmin): # класс для кастомизации
 #   list_display = ["name", "email"] #Выбор полей для вывода
    list_display = [field.name for field in Subscriber._meta.fields] # вывод всех данных в админку
    #exclude = ["name"] #Исключить из меню добавления и когда заходим в продробно
    #fields = ["name"] #обратное exclude(показывать только)
    #list_filter = ("name",) #справа появляется фильтр по имени(не забедь запятую)!
    #search_fields = ["name", "email"]#добавление сверху поиска, который позволяет искать по имени
    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin) #Первый это наше из моделс 2 создаем и опысаем тут же выше

