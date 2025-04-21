from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),
    path('novo/', views.criar_contato, name='criar_contato'),
    path('delete/<int:contato_id>/', views.deletar_contato, name='deletar_contato'),
]
