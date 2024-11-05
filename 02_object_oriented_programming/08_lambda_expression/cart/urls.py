# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('calculate_total/', views.calculate_total, name='calculate_total'),
]
