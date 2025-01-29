from django.shortcuts import render

def index_view(request):
    return render(request, 'fourth_task/index.html', {'pagename': 'Главная страница'})

def shop_view(request):
    items = [
        {'name': 'Смеситель', 'price':15000},
        {'name': 'Унитаз', 'price':25000},
        {'name': 'Ванна', 'price':65000},
    ]
    return render(request, 'fourth_task/shop.html', {'pagename': 'Магазин', 'items': items})

def cart_view(request):
    return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина'})


