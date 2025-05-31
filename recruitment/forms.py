from django import forms
from .models import *

# TODO: Define form fields here
class DepartemenForm(forms.ModelForm):
    """Form definition for Departemen."""

    class Meta:
        """Meta definition for Departemenform."""

        model = Departemen
        fields = '__all__'

