from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.
    
LIST_GENDER_PERTEKER = (
    ('Perempuan', 'Perempuan'),
    ('Laki-laki', 'Laki-laki'),
    ('Laki-laki/Perempuan', 'Laki-laki/Perempuan')
)

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

LIST_HASIL_TEST = (
    ('Baik', 'Baik'),
    ('Cukup', 'Cukup'),
    ('Kurang', 'Kurang')
)

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
   
    # TODO: Define fields here
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    gender          = models.CharField(
                        max_length = 20,
                        choices = LIST_GENDER_PERTEKER,
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
        return f"{self.user.username}-{self.open_poss}-{self.batas_usia}-{self.pendidikan_min}-{self.pengalaman}"

class Pelamar(models.Model):
    """Model definition for Pelamar."""

    # TODO: Define fields here
    nama        = models.CharField(max_length = 64)
    gender      = models.CharField(
                        max_length = 12,
                        choices = LIST_GENDER,
                        default = 'Laki-laki'
                    )
    usia        = models.IntegerField()
    pendidikan  = models.CharField(
                        max_length = 12,
                        choices = LIST_PENDIDIKAN,
                        default = 'SMA/SMK/MA'
                    )
    jurusan     = models.CharField(max_length = 64)
    almamater   = models.CharField(max_length = 64)
    pengalaman  = models.CharField(
                        max_length = 8,
                        choices = LIST_EXP,
                        default = 'Tidak'
                    )
    keahlian    = models.CharField(max_length = 32)
    perteker    = models.ForeignKey(Perteker, on_delete = models.CASCADE, null = True, blank = True)
    alamat      = models.CharField(max_length = 100)
    phone       = models.CharField(max_length = 16)
    tanggal     = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        """Meta definition for Pelamar."""

        verbose_name = 'Pelamar'
        verbose_name_plural = 'Pelamars'

    def __str__(self):
        """Unicode representation of Pelamar."""
        return f"{self.nama}-{self.gender}-{self.usia}-{self.pendidikan}-{self.pengalaman}"

class Seleksi(models.Model):
    """Model definition for Seleksi."""

    # TODO: Define fields here
    pelamar         = models.ForeignKey(Pelamar, on_delete = models.CASCADE)
    nilai_psikotest = models.CharField(
                            max_length = 8,
                            choices = LIST_HASIL_TEST,
                            blank = True
                        )
    nilai_interview = models.CharField(
                            max_length = 8,
                            choices = LIST_HASIL_TEST,
                            blank = True
                        )
    status          = models.CharField(max_length = 8, blank = True)
    catatan         = models.CharField(max_length = 64, blank = True)
    tanggal         = models.DateField(auto_now = True)

    class Meta:
        """Meta definition for Seleksi."""

        verbose_name = 'Seleksi'
        verbose_name_plural = 'Seleksis'

    def __str__(self):
        """Unicode representation of Seleksi."""
        return f"{self.pelamar.nama}-{self.nilai_psikotest}{self.nilai_interview}-{self.status}"
