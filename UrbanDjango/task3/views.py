# task3/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = [
        {'name': 'Смеситель', 'price':15000},
        {'name': 'Унитаз', 'price':25000},
        {'name': 'Ванна', 'price':65000},
    ]
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
