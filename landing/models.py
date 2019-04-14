# Создание модели
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)


# Вывод опеределенных строк в поля в админке
    def __str__(self):
        return "User %s %s" % (self.name, self.email)

# Название таблиц в admin в ед числе и множественном
    class Meta:
        verbose_name = 'MySub'
        verbose_name_plural = 'Subs'