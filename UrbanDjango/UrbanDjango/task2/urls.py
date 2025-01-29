from django.urls import path
from .views import ClassView, function_view

urlpatterns = [
    path('class/', ClassView.as_view(), name='class_view'),
    path('function/', function_view, name='function_view'),
]

