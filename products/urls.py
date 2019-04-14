from django.conf.urls import re_path
from products import views

urlpatterns = [
    # url(r'^landing123/', views.landing, name='landing'),
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]