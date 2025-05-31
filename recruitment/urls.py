from django.urls import path
from recruitment import views

app_name = 'recruitment'
urlpatterns = [
    path('departemen', views.listDepartemen, name = 'list_departemen'),
    path('pelamar', views.listPelamar, name = 'list_pelamar'),
    path('perteker', views.listPerteker, name = 'liast_perteker'),
    path('seleksi', views.listSeleksi, name = 'list_seleksi')
]