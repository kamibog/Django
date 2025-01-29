# task3/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        'item1': 'Смеситель',
        'item2': 'Унитаз',
        'item3': 'Ванна',
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
