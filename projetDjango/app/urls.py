from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('read', views.read, name='read'),
    path('read/<id>', views.read_detail, name='read_detail'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update, name='update'),
    path('update/updateproduct/<id>', views.updateproduct, name='updateproduct'),
]
