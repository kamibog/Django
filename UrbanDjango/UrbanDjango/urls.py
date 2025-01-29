# UrbanDjango/urls.py
from django.contrib import admin
from django.urls import path
from task3.views import index, shop, cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
]



'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/class/', ClassView.as_view(), name='class_view'),
    path('task2/function/', function_view, name='function_view'),
    path('', ClassView.as_view(), name='home'),
]'''




