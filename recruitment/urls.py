from django.urls import path
from recruitment import views

urlpatterns = [
    path('seleksi', views.listSeleksi, name='list_seleksi')
]