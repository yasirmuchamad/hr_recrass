from django import forms
from .models import *

# TODO: Define form fields here
class DepartemenForm(forms.ModelForm):
    """Form definition for Departemen."""

    class Meta:
        """Meta definition for Departemenform."""

        model = Departemen
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DepartemenForm, self).__init__(*args, **kwargs)
        self.fields["nama"].widget.attrs.update({'id': 'nama', 'name':'nama',
                                                 'class':'form-control', 'placeholder':'Input Nama Departemen'})


class PelamarForm(forms.ModelForm):
    """Form definition for Departemen."""

    class Meta:
        """Meta definition for Departemenform."""

        model = Pelamar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PelamarForm, self).__init__(*args, **kwargs)
        self.fields["nama"].widget.attrs.update({'id': 'nama', 'name':'nama',
                                                 'class':'form-control', 'placeholder':'Input Nama Pelamar'})
        self.fields["gender"].widget.attrs.update({'id': 'gender', 'name':'gender',
                                                 'class':'form-control'})
        self.fields["usia"].widget.attrs.update({'id': 'usia', 'name':'usia',
                                                 'class':'form-control', 'placeholder':'Input Usia Pelamar'})
        self.fields["pendidikan"].widget.attrs.update({'id': 'pendidikan', 'name':'pendidikan',
                                                 'class':'form-control', 'placeholder':'Input Pendidikan Tearakhir Pelamar'})
        self.fields["jurusan"].widget.attrs.update({'id': 'jurusan', 'name':'jurusan',
                                                 'class':'form-control', 'placeholder':'Input Jurusan Pelamar'})
        self.fields["almamater"].widget.attrs.update({'id': 'almamater', 'name':'almamater',
                                                 'class':'form-control', 'placeholder':'Input Keahlian Pelamar'})
        self.fields["pengalaman"].widget.attrs.update({'id': 'pengalaman', 'name':'pengalaman',
                                                 'class':'form-control', 'placeholder':'Input Pendidikan Pelamar'})
        self.fields["keahlian"].widget.attrs.update({'id': 'keahlian', 'name':'keahlian',
                                                 'class':'form-control', 'placeholder':'Input Keahlian Pelamar'})
        self.fields["perteker"].widget.attrs.update({'id': 'perteker', 'name':'perteker',
                                                 'class':'form-control'})
        self.fields["alamat"].widget.attrs.update({'id': 'alamat', 'name':'alamat',
                                                 'class':'form-control', 'placeholder':'Input Alamat Pelamar'}) 
        self.fields["phone"].widget.attrs.update({'id': 'phone', 'name':'phone',
                                                 'class':'form-control', 'placeholder':'Input Nomor Telephon/WhatsApp Pelamar'}) 


class PertekerForm(forms.ModelForm):
    """Form definition for Departemen."""

    class Meta:
        """Meta definition for Departemenform."""

        model = Perteker
        fields = '__all__'

    def __init__(self, *args, user=None, **kwargs):
        super(PertekerForm, self).__init__(*args, **kwargs)
        # self.fields["user"].widget.attrs.update({'id': 'user', 'name':'user',
        #                                          'class':'form-control'})
        self.fields["gender"].widget.attrs.update({'id': 'gender', 'name':'gender',
                                                 'class':'form-control'})
        self.fields["open_poss"].widget.attrs.update({'id': 'posisi', 'name':'posisi',
                                                 'class':'form-control', 'placeholder':'Input Posisi'})
        self.fields["batas_usia"].widget.attrs.update({'id': 'usia', 'name':'usia',
                                                 'class':'form-control', 'placeholder':'Input Usia'})
        self.fields["pendidikan_min"].widget.attrs.update({'id': 'pendidikan', 'name':'pendidikan',
                                                 'class':'form-control', 'placeholder':'Input Pendidikan'})
        self.fields["jurusan"].widget.attrs.update({'id': 'jurusan', 'name':'jurusan',
                                                 'class':'form-control', 'placeholder':'Input Jurusan'})
        self.fields["pengalaman"].widget.attrs.update({'id': 'pengalaman', 'name':'pengalaman',
                                                 'class':'form-control'})
        self.fields["jumlah"].widget.attrs.update({'id': 'jumlah', 'name':'jumlah',
                                                 'class':'form-control', 'placeholder':'Input jumlah Kebutuhan'})