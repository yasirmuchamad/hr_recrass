from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(Departemen)
class DepartemenAdmin(admin.ModelAdmin):
    list_display = ['nama']

@admin.register(Perteker)
class PertekerAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'open_poss', 'batas_usia', 'pendidikan_min', 'pengalaman']

@admin.register(Pelamar)
class PelamarAdmin(admin.ModelAdmin):
    list_display = ['nama', 'gender', 'usia', 'pendidikan', 'almamater', 'jurusan', 'pengalaman', 'keahlian', 'perteker', 'alamat', 'phone']

@admin.register(Seleksi)
class SeleksiAdmin(admin.ModelAdmin):
    list_display = ['pelamar', 'nilai_psikotest', 'nilai_interview', 'status']
