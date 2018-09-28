from django.urls import path
from .views import *

app_name = 'orders'
urlpatterns = [
    # VBF
    path('clientes/', list_client, name='clients'),
    path('clientes/crear/', create_client, name='create_client'),
    path('clientes/editar/<int:pk>', edit_client, name='edit_client'),
    path('clientes/detalle/<int:pk>', detail_client, name='detail_client'),
    path('clientes/eliminar/<int:pk>', delete_client, name='delete_client'),
    
    # VBC
    # path('clients/', ListClientView.as_view(), name='list_client'),
    # path('clients/create/', CreateClientView.as_view(), name='register_client'),
    # path('clients/detail/<int:pk>', DetailClientView.as_view(), name='detail_client'),
    # path('clients/edit/<int:pk>', edit_client, name='edit_client'),
]