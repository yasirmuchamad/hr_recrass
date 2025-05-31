from django.urls import path
from recruitment import views

app_name = 'recruitment'
urlpatterns = [
    path('departemen', views.listDepartemen, name = 'list_departemen'),
    path('departemen/add', views.createDepartemen, name = 'create_departemen'),
    path('departemen/update/<int:update_id>', views.updateDepartemen, name = 'update_departemen'),
    path('departemen/delete/<int:delete_id>', views.deleteDepartemen, name = 'delete_departemen'),

    path('pelamar', views.listPelamar, name = 'list_pelamar'),
    path('pelamar/add', views.createPelamar, name = 'create_pelamar'),
    path('pelamar/update/<int:update_id>', views.updatePelamar, name = 'update_pelamar'),
    # path('pelamar/delete/<int:delete_id>', views.deletePelamar, name = 'delete_pelamar'),

    path('perteker', views.listPerteker, name = 'list_perteker'),
    path('seleksi', views.listSeleksi, name = 'list_seleksi')
]