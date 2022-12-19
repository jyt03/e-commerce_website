from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.grocery),
    path('products/cart/', views.cart),

]
