# Generated by Django 5.2.1 on 2025-06-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0004_rename_departemen_customuser_departemen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seleksi',
            name='nilai_interview',
            field=models.CharField(blank=True, choices=[('Baik', 'Baik'), ('Cukup', 'Cukup'), ('Kurang', 'Kurang')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='seleksi',
            name='nilai_psikotest',
            field=models.CharField(blank=True, choices=[('Baik', 'Baik'), ('Cukup', 'Cukup'), ('Kurang', 'Kurang')], max_length=8, null=True),
        ),
    ]
