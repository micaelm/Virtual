from django.urls import path
from .views import index,estoque

urlpatterns = [
    path('', index, name='index'),
    path('estoque/<int:pk>', estoque, name='estoque'),
]
