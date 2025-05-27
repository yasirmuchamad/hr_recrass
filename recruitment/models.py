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