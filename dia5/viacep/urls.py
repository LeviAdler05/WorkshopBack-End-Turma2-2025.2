from django.urls import path
from .views import (
    EnderecoCreateView, EnderecoListView, EnderecoDetailView,
    EnderecoDeleteView
)

app_name = 'viacep'

urlpatterns = [
    path('', EnderecoCreateView.as_view(), name='create'),
    path('listar/', EnderecoListView.as_view(), name='list'),
    path('<int:pk>/', EnderecoDetailView.as_view(), name='detail'),
    path('<int:pk>/excluir/', EnderecoDeleteView.as_view(), name='delete'),
]