from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('delete/<int:id>', views.delete_id, name='delete_id'),
]