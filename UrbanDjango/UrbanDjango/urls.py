from django.urls import path
from task4.views import index_view, shop_view, cart_view

urlpatterns = [
    path('', index_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
]




'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/class/', ClassView.as_view(), name='class_view'),
    path('task2/function/', function_view, name='function_view'),
    path('', ClassView.as_view(), name='home'),
]'''




