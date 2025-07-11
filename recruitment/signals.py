from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender = Pelamar)
def createSeleksiFromPelamar(sender, instance, created, **kwargs):
    if created:
        Seleksi.objects.create(
            pelamar         = instance,
            nilai_psikotest = None,
            nilai_interview = None,
            status          = 'Belum diproses',
            catatan         = None
        )