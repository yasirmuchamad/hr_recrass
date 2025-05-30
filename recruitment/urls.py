from django.urls import path
from recruitment import views

app_name = 'recruitment'
urlpatterns = [
    path('departemen', views.listDepartemen, name = 'list_departemen'),
    path('seleksi', views.listSeleksi, name = 'list_seleksi')
]