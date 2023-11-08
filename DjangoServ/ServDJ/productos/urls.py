from django.urls import path
from . import views

urlpatterns = [
    path('lista-productos/', views.lista_productos, name='lista_productos'),
]