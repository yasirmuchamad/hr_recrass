from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.

class Departemen(models.Model):
    """Model definition for Departemen."""

    # TODO: Define fields here
    nama    = models.CharField(max_length = 32)
    class Meta:
        """Meta definition for Departemen."""

        verbose_name = 'Departemen'
        verbose_name_plural = 'Departemens'

    def __str__(self):
        """Unicode representation of Departemen."""
        return self.nama

class CustomUser(AbstractUser):
    Departemen  = models.ForeignKey(Departemen, on_delete = models.CASCADE, null = True, blank = True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.groups.exists():
            default_group, created = Group.objects.get_or_create(name = 'User')
            self.groups.add(default_group)
            print("user berhasil disimpan")

    def __str__(self):
        return f"{self.username} | {self.first_name} | {self.last_name}"

class Perteker(models.Model):
    """Model definition for Perteker."""
    LIST_GENDER = (
        ('Perempuan', 'Perempuan'),
        ('Laki-laki', 'Laki-laki')
    )

    LIST_EXP = (
        ('Ya', 'Ya'),
        ('Tidak', 'Tidak')
    )

    LIST_PENDIDIKAN = (
        ('SD/MI', 'SD/MI'),
        ('SMP/MTS', 'SMP/MTS'),
        ('SMA/SMK/MA', 'SMA/SMK/MA'),
        ('D3', 'D3'),
        ('D4', 'D4'),
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3')
    )

    # TODO: Define fields here
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    gender          = models.CharField(
                        max_length = 12,
                        choices = LIST_GENDER,
                        default = 'Laki-laki'
                        )
    open_poss       = models.CharField(max_length = 32)
    batas_usia      = models.IntegerField()
    pendidikan_min  = models.CharField(
                        max_length = 12,
                        choices = LIST_PENDIDIKAN,
                        default = 'SMA/SMK/MA'
                        )
    jurusan         = models.CharField(max_length = 64)
    pengalaman      = models.CharField(
                        max_length = 8,
                        choices = LIST_EXP,
                        default = 'Tidak'
                        )
    jumlah          = models.IntegerField()
    tanggal         = models.DateTimeField(auto_now_add = True)

    class Meta:
        """Meta definition for Perteker."""

        verbose_name = 'Perteker'
        verbose_name_plural = 'Pertekers'

    def __str__(self):
        """Unicode representation of Perteker."""
        return f"{self.user.name}-{self.open_poss}-{self.batas_usia}-{self.pendidikan_min}-{self.pengalaman}"
