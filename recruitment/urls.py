from django.urls import path
from recruitment import views

app_name = 'recruitment'
urlpatterns = [
    path('index', views.index, name='index'),

    path('departemen', views.listDepartemen, name = 'list_departemen'),
    path('departemen/add', views.createDepartemen, name = 'create_departemen'),
    path('departemen/update/<int:update_id>', views.updateDepartemen, name = 'update_departemen'),
    path('departemen/delete/<int:delete_id>', views.deleteDepartemen, name = 'delete_departemen'),
    path('departemen/export', views.departemenExcel, name='export_excel_departemen'),

    path('pelamar', views.listPelamar, name = 'list_pelamar'),
    path('pelamar/add', views.createPelamar, name = 'create_pelamar'),
    path('pelamar/update/<int:update_id>', views.updatePelamar, name = 'update_pelamar'),
    path('pelamar/delete/<int:delete_id>', views.deletePelamar, name = 'delete_pelamar'),
    path('pelamar/export', views.pelamarExcel, name='export_excel_pelamar'),

    path('perteker', views.listPerteker, name = 'list_perteker'),
    path('perteker/add', views.createPerteker, name = 'create_perteker'),
    path('perteker/update/<int:update_id>', views.updatePerteker, name = 'update_perteker'),
    path('perteker/delete/<int:delete_id>', views.deletePerteker, name = 'delete_perteker'),
    path('perteker/export', views.pertekerExcel, name='export_excel_perteker'),

    path('seleksi', views.listSeleksi, name = 'list_seleksi'),
    path('seleksi/update/<int:update_id>', views.updateSeleksi, name = 'update_seleksi'),
    path('seleksi/export', views.seleksiExcel, name='export_excel_seleksi'),

    path('user', views.list_user, name='list_user'),
    path('user/create_user', views.create_user, name='create_user'),
    path('user/update_user/<int:update_id>', views.update_user, name='update_user'),
    path('user/delete_user/<int:delete_id>', views.delete_user, name='delete_user'),
    path('user/export', views.userExcel, name='export_excel_user'),

    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]