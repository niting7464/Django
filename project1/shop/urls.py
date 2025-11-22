from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('about/', views.products, name='shop-products'),
]