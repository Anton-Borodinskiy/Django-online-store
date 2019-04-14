from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline): # !!!! Добавление фото снизу в классе
    model = ProductImage
    extra = 0

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin (admin.ModelAdmin): # класс для кастомизации
    list_display = [field.name for field in Product._meta.fields] # вывод всех данных в админку
    inlines = [ProductImageInline] # !!!! Добавление фото снизу в классе
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin) #Первый это наше из моделс 2 создаем и опысаем тут же выше


class ProductImageAdmin (admin.ModelAdmin): # класс для кастомизации
    list_display = [field.name for field in ProductImage._meta.fields] # вывод всех данных в админку
    class Meta:
        model = ProductImage
admin.site.register(ProductImage, ProductImageAdmin) #Первый это наше из моделс 2 создаем и опысаем тут же выше