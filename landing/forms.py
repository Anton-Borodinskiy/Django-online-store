# Создание формы
from django import forms
from . models import *


class AddSubscriber(forms.ModelForm):

    class Meta:
        model = Subscriber #Название модели
        exclude = [""]