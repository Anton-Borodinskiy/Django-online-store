from django.shortcuts import render
from products.models import *


def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    session_key = request.session.session_key


    return render(request, 'landing/home.html', locals())

def clothing(request):
    session_key = request.session.session_key
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_clothings = products_images.filter(product__category__id=4)
    return render(request, 'landing/clothing.html', locals()) #дефолт

def shoes(request):
    session_key = request.session.session_key
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_shoes = products_images.filter(product__category__id=2)
    return render(request, 'landing/shoes.html', locals()) #дефолт

def accesories(request):
    session_key = request.session.session_key
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_accesories = products_images.filter(product__category__id=3)
    return render(request, 'landing/accesories.html', locals()) #дефолт