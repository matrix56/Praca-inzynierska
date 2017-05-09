from django import forms

from .models import lekarze

class LekarzeForm(forms.ModelForm):

    class Meta:
        model=Doctor
        fields=('Imie', 'Nazwisko',)
