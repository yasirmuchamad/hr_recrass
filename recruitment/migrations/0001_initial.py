# Generated by Django 5.2.1 on 2025-05-28 11:16

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departemen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Departemen',
                'verbose_name_plural': 'Departemens',
            },
        ),
        migrations.CreateModel(
            name='Pelamar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('Perempuan', 'Perempuan'), ('Laki-laki', 'Laki-laki')], default='Laki-laki', max_length=12)),
                ('usia', models.IntegerField()),
                ('pendidikan', models.CharField(choices=[('SD/MI', 'SD/MI'), ('SMP/MTS', 'SMP/MTS'), ('SMA/SMK/MA', 'SMA/SMK/MA'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], default='SMA/SMK/MA', max_length=12)),
                ('jurusan', models.CharField(max_length=64)),
                ('almamater', models.CharField(max_length=64)),
                ('pengalaman', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], default='Tidak', max_length=8)),
                ('keahlian', models.CharField(max_length=32)),
                ('alamat', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=16)),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pelamar',
                'verbose_name_plural': 'Pelamars',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('Departemen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruitment.departemen')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Perteker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Perempuan', 'Perempuan'), ('Laki-laki', 'Laki-laki')], default='Laki-laki', max_length=12)),
                ('open_poss', models.CharField(max_length=32)),
                ('batas_usia', models.IntegerField()),
                ('pendidikan_min', models.CharField(choices=[('SD/MI', 'SD/MI'), ('SMP/MTS', 'SMP/MTS'), ('SMA/SMK/MA', 'SMA/SMK/MA'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], default='SMA/SMK/MA', max_length=12)),
                ('jurusan', models.CharField(max_length=64)),
                ('pengalaman', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], default='Tidak', max_length=8)),
                ('jumlah', models.IntegerField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perteker',
                'verbose_name_plural': 'Pertekers',
            },
        ),
        migrations.CreateModel(
            name='Seleksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai_psikotest', models.CharField(blank=True, choices=[('Baik', 'Baik'), ('Cukup', 'Cukup'), ('Kurang', 'Kurang')], max_length=8)),
                ('nilai_interview', models.CharField(blank=True, choices=[('Baik', 'Baik'), ('Cukup', 'Cukup'), ('Kurang', 'Kurang')], max_length=8)),
                ('status', models.CharField(blank=True, max_length=8)),
                ('catatan', models.CharField(blank=True, max_length=64)),
                ('tanggal', models.DateField(auto_now=True)),
                ('pelamar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.pelamar')),
            ],
            options={
                'verbose_name': 'Seleksi',
                'verbose_name_plural': 'Seleksis',
            },
        ),
    ]
