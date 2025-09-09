from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultar_enderecos, name='consultar_enderecos'),
]
