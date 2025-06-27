from django import forms
from .models import *
# from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# TODO: Define form fields here
class CustomUserCreationForm(UserCreationForm):
    departemen = forms.ModelChoiceField(
        queryset = Departemen.objects.all(),
        empty_label = "Pilih Departemen"
    )
    # departement = forms.ModelChoiceField(queryset=Departement.objects.all(), empty_label="Select Department")
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'departemen']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'id': 'username', 'name':'username',
                                                 'class':'form-control', 'placeholder':'Input username'})
        self.fields["email"].widget.attrs.update({'id': 'email', 'name':'email',
                                                 'class':'form-control', 'placeholder':'Input Email'})
        self.fields["first_name"].widget.attrs.update({'id': 'first_name', 'name':'first_name',
                                                 'class':'form-control', 'placeholder':'Input first_name'})
        self.fields["last_name"].widget.attrs.update({'id': 'last_name', 'name':'last_name',
                                                 'class':'form-control', 'placeholder':'Input last_name'})
        self.fields["password1"].widget.attrs.update({'id': 'password1', 'name':'password1',
                                                 'class':'form-control', 'placeholder':'type your password'})
        self.fields["password2"].widget.attrs.update({'id': 'password2', 'name':'password2',
                                                 'class':'form-control', 'placeholder':'retype your password'})
        self.fields["departemen"].widget.attrs.update({'id': 'departemen', 'name':'departemen',
                                                 'class':'form-control'})


class CustomUserUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'departemen']

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'id': 'username', 'name':'username',
                                                 'class':'form-control', 'placeholder':'Input username'})
        self.fields["email"].widget.attrs.update({'id': 'email', 'name':'email',
                                                 'class':'form-control', 'placeholder':'Input Email'})
        self.fields["first_name"].widget.attrs.update({'id': 'first_name', 'name':'first_name',
                                                 'class':'form-control', 'placeholder':'Input first_name'})
        self.fields["last_name"].widget.attrs.update({'id': 'last_name', 'name':'last_name',
                                                 'class':'form-control', 'placeholder':'Input last_name'})
        self.fields["departemen"].widget.attrs.update({'id': 'departemen', 'name':'departemen',
                                                 'class':'form-control', 'placeholder':'Input departemen'})


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
        # fields = '__all__'
        exclude = ['user']

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