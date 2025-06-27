from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    # masukkan field tambahan kedalam fieldset
    fieldsets = (
        (None, {
            'fields': (
                'username', 'password'
            ),
        }),
        (_('personal imfo'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields':('last_login', "date_joined")}),
    )
    add_fieldset = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }
        ),
    )
    list_display = ['username', 'email', 'is_staff', 'get_groups']

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()]) if obj.groups.exists() else "No Group"
    
    get_groups.short_description = 'groups'

@admin.register(Departemen)
class DepartemenAdmin(admin.ModelAdmin):
    list_display = ['nama']

@admin.register(Perteker)
class PertekerAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'open_poss', 'batas_usia', 'pendidikan_min', 'pengalaman']

@admin.register(Pelamar)
class PelamarAdmin(admin.ModelAdmin):
    list_display = ['nama', 'gender', 'usia', 'pendidikan', 'almamater', 'jurusan', 'pengalaman', 'keahlian', 'perteker', 'alamat', 'phone','tanggal']

@admin.register(Seleksi)
class SeleksiAdmin(admin.ModelAdmin):
    list_display = ['pelamar', 'nilai_psikotest', 'nilai_interview', 'status', 'tanggal']
